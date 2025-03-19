import subprocess

def run_powershell(command):
    """Exécute une commande PowerShell et retourne la sortie."""
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    return result.stdout.strip() if result.stdout else result.stderr.strip()

def list_vms():
    """Liste les machines virtuelles disponibles."""
    print("\n🔍 Liste des VM Azure...\n")
    command = "Get-AzVM | Select-Object Name, ResourceGroupName | Format-Table -AutoSize"
    output = run_powershell(command)
    
    if output:
        print(output)
    else:
        print("⚠️ Aucune VM trouvée.")

def create_vm():
    """Crée une machine virtuelle avec PowerShell."""
    name = input("\n🔹 Nom de la nouvelle VM : ")
    rg = input("🔹 Nom du Resource Group : ")
    location = input("🔹 Région (ex: westeurope) : ")
    size = "Standard_B2s"  # Taille correcte

    # Image Debian 12 correcte
    publisher = "Debian"
    offer = "debian-12"
    sku = "12-gen2"

    print("\n🚀 Création de la VM en cours...\n")

    command = f"""
    $password = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force
    $credential = New-Object System.Management.Automation.PSCredential ("azureuser", $password)

    # Création de l'adresse IP publique
    $publicIp = New-AzPublicIpAddress -ResourceGroupName {rg} -Name "{name}-ip" -Location {location} -AllocationMethod Dynamic

    # Création du réseau virtuel
    $vnet = New-AzVirtualNetwork -ResourceGroupName {rg} -Name "{name}-vnet" -Location {location} -AddressPrefix "10.0.0.0/16"
    $subnet = Add-AzVirtualNetworkSubnetConfig -Name "default" -AddressPrefix "10.0.0.0/24" -VirtualNetwork $vnet
    $vnet | Set-AzVirtualNetwork

    # Création de l'interface réseau
    $nic = New-AzNetworkInterface -ResourceGroupName {rg} -Name "{name}-nic" -Location {location} -SubnetId $subnet.Id -PublicIpAddressId $publicIp.Id

    # Configuration de la VM
    $vmConfig = New-AzVMConfig -VMName {name} -VMSize '{size}'
    $vmConfig = Set-AzVMOperatingSystem -VM $vmConfig -Linux -Credential $credential -ComputerName {name}
    $vmConfig = Set-AzVMSourceImage -VM $vmConfig -PublisherName '{publisher}' -Offer '{offer}' -Skus '{sku}' -Version 'latest'
    $vmConfig = Add-AzVMNetworkInterface -VM $vmConfig -Id $nic.Id

    # Création de la VM
    New-AzVM -ResourceGroupName {rg} -Location {location} -VM $vmConfig
    """
    
    output = run_powershell(command)
    print("\n📝 DEBUG: Commande PowerShell exécutée :\n", command)
    print("\n📝 DEBUG: Résultat PowerShell :\n", output)

    # Vérification après création avec un délai pour éviter un faux négatif
    print("\n🔍 Vérification de la VM...\n")
    check_command = f"Start-Sleep -Seconds 10; Get-AzVM -ResourceGroupName {rg} -Name {name} | Select-Object Name"
    check_output = run_powershell(check_command)
    
    if name in check_output:
        print(f"✅ VM '{name}' créée avec succès et disponible !")
    else:
        print("❌ La VM ne semble pas avoir été créée. Vérifie les logs Azure.")

def delete_vm():
    """Supprime une machine virtuelle."""
    name = input("\n❌ Nom de la VM à supprimer : ")
    rg = input("❌ Nom du Resource Group : ")

    print("\n🛑 Suppression en cours...\n")
    command = f"Remove-AzVM -Name {name} -ResourceGroupName {rg} -Force"
    
    output = run_powershell(command)
    print("\n📝 DEBUG: Commande PowerShell exécutée :\n", command)
    print("\n📝 DEBUG: Résultat PowerShell :\n", output)

    print(f"\n✅ VM '{name}' supprimée !")

# Menu principal
while True:
    print("\n💠 Menu Azure VM 💠")
    print("1️⃣ Lister les VM")
    print("2️⃣ Créer une VM")
    print("3️⃣ Supprimer une VM")
    print("0️⃣ Quitter")

    choix = input("\n🔹 Ton choix : ")

    if choix == "1":
        list_vms()
    elif choix == "2":
        create_vm()
    elif choix == "3":
        delete_vm()
    elif choix == "0":
        print("👋 Bye !")
        break
    else:
        print("❌ Choix invalide, recommence.")
