import subprocess
import json

def run_powershell(command):
    """Exécute une commande PowerShell et retourne la sortie JSON."""
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    return result.stdout.strip()

def list_vms():
    """Liste toutes les VM disponibles dans Azure."""
    print("\n🔍 Récupération des machines virtuelles...")
    command = "Get-AzVM | ConvertTo-Json -Depth 2"
    output = run_powershell(command)

    if not output:
        print("⚠️ Aucune VM trouvée.")
        return []

    try:
        vms = json.loads(output)
        if isinstance(vms, dict):  # Si une seule VM, on la met dans une liste
            vms = [vms]
        
        print("\n📌 Machines virtuelles disponibles :")
        for vm in vms:
            print(f"- {vm['Name']} ({vm['ResourceGroupName']})")
        
        return vms
    except json.JSONDecodeError:
        print("❌ Erreur lors du parsing des données.")
        return []

def create_vm():
    """Crée une nouvelle VM en demandant les paramètres à l'utilisateur."""
    name = input("\n🆕 Nom de la nouvelle VM : ").strip()
    rg = input("📂 Nom du Resource Group : ").strip()
    location = input("🌍 Région (ex: eastus, westeurope) : ").strip()
    size = input("💾 Taille de la VM (ex: Standard_B1s) : ").strip()
    image = input("📦 Image OS (ex: UbuntuLTS, Win2022Datacenter) : ").strip()

    command = f"""
    New-AzVM -ResourceGroupName {rg} -Name {name} -Location {location} `
             -Size {size} -Image {image} -Credential (Get-Credential)
    """

    print("\n🚀 Création de la VM en cours...")
    run_powershell(command)
    print(f"✅ VM {name} créée avec succès !")

def delete_vm():
    """Supprime une VM existante."""
    vms = list_vms()
    if not vms:
        return

    name = input("\n❌ Nom de la VM à supprimer : ").strip()
    rg = input("📂 Nom du Resource Group : ").strip()

    confirm = input(f"⚠️ Es-tu sûr de vouloir supprimer {name} ? (oui/non) : ").strip().lower()
    if confirm != "oui":
        print("🚫 Annulation de la suppression.")
        return

    command = f"Remove-AzVM -Name {name} -ResourceGroupName {rg} -Force"
    print("\n🗑️ Suppression en cours...")
    run_powershell(command)
    print(f"✅ VM {name} supprimée avec succès !")

# --- Menu ---
while True:
    print("\n=== 🖥️ Gestion des VM Azure ===")
    print("1️⃣ Lister les VM")
    print("2️⃣ Créer une VM")
    print("3️⃣ Supprimer une VM")
    print("0️⃣ Quitter")

    choice = input("🔹 Que veux-tu faire ? ").strip()
    
    if choice == "1":
        list_vms()
    elif choice == "2":
        create_vm()
    elif choice == "3":
        delete_vm()
    elif choice == "0":
        print("👋 Au revoir !")
        break
    else:
        print("❌ Option invalide, réessaie.")
