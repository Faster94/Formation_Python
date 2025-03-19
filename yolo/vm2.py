import subprocess
import json

def run_powershell(command):
    """Exécute une commande PowerShell et retourne la sortie JSON."""
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    return result.stdout.strip()

def list_vms():
    """Liste les VMs existantes."""
    print("\n📜 Liste des VMs Azure :")
    command = "Get-AzVM | Select-Object Name, ResourceGroupName | ConvertTo-Json -Depth 1"
    output = run_powershell(command)

    if not output:
        print("⚠️ Aucune VM trouvée.")
        return

    try:
        vms = json.loads(output)

        # Si une seule VM est retournée, elle est un dict et non une liste
        if isinstance(vms, dict):
            vms = [vms]

        for vm in vms:
            print(f"🖥️ {vm.get('Name', 'N/A')} (RG: {vm.get('ResourceGroupName', 'N/A')})")

    except json.JSONDecodeError:
        print("❌ Erreur lors de la récupération des VMs. Vérifie que ton compte est bien connecté à Azure.")

def create_vm():
    """Crée une nouvelle VM avec des paramètres fixes."""
    name = input("\n🆕 Nom de la nouvelle VM : ").strip()
    rg = input("📂 Nom du Resource Group : ").strip()
    location = input("🌍 Région (ex: eastus, westeurope) : ").strip()
    size = input("💾 Taille de la VM (ex: Standard_B1s) : ").strip()
    image = input("📦 Image OS (ex: UbuntuLTS, Win2022Datacenter) : ").strip()

    command = f"""
    $password = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force
    $credential = New-Object System.Management.Automation.PSCredential ("azureuser", $password)
    New-AzVM -ResourceGroupName {rg} -Name {name} -Location {location} `
             -Size {size} -Image {image} -Credential $credential
    """

    print("\n🚀 Création de la VM en cours...")
    run_powershell(command)
    output_debug = run_powershell(command)
    print("\n📝 DEBUG: Commande PowerShell exécutée :\n", command)
    print("\n📝 DEBUG: Résultat PowerShell :\n", output_debug)


    print("\n🔍 Vérification de la VM...")
    check_command = f"Get-AzVM -Name {name} -ResourceGroupName {rg} | ConvertTo-Json -Depth 1"
    output = run_powershell(check_command)

    if output:
        print(f"✅ VM {name} créée avec succès !")
    else:
        print("❌ La VM ne semble pas avoir été créée. Vérifie les logs Azure.")

def delete_vm():
    """Supprime une VM existante."""
    name = input("\n❌ Nom de la VM à supprimer : ").strip()
    rg = input("📂 Nom du Resource Group : ").strip()
    command = f"Remove-AzVM -Name {name} -ResourceGroupName {rg} -Force"
    print("\n🗑️ Suppression en cours...")
    run_powershell(command)
    print(f"✅ VM {name} supprimée.")

while True:
    print("\n🔹 Menu :")
    print("1️⃣ Lister les VMs")
    print("2️⃣ Créer une VM")
    print("3️⃣ Supprimer une VM")
    print("4️⃣ Quitter")
    
    choix = input("\n👉 Choix : ").strip()
    
    if choix == "1":
        list_vms()
    elif choix == "2":
        create_vm()
    elif choix == "3":
        delete_vm()
    elif choix == "4":
        print("👋 Fin du programme.")
        break
    else:
        print("❌ Choix invalide, réessaie.")


