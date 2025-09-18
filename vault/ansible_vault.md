# Ansible Vault Guide

Ansible Vault is a feature that allows you to **encrypt and protect sensitive data** such as passwords, API keys, SSH keys, and certificates.  
It ensures that secrets are stored securely in playbooks, roles, and variable files.

---

## 1. Why Use Ansible Vault?

- Securely store **secrets** (passwords, tokens, keys).
- Prevent exposing sensitive data in Git repositories.
- Encrypt entire files or just specific variables.
- Easily decrypt when running playbooks.

---

## 2. Creating an Encrypted File

You can create a new encrypted file using:

```bash
ansible-vault create secrets.yml
```

- It will ask for a **password**.
- Opens the file in an editor (like `vim`) where you can add secrets.

**Example (`secrets.yml` after encryption):**
```
$ANSIBLE_VAULT;1.1;AES256
31326361656634356434346538363765643738626531336430393333326632343162663738393865
...
```

---

## 3. Encrypting an Existing File

If you already have a file with sensitive data, you can encrypt it:

```bash
ansible-vault encrypt vars.yml
```

---

## 4. Decrypting a File

To view or edit the file later:

```bash
ansible-vault decrypt secrets.yml
```

Or just edit without fully decrypting:

```bash
ansible-vault edit secrets.yml
```

---

## 5. Viewing Encrypted Files

You can view an encrypted file without editing:

```bash
ansible-vault view secrets.yml
```

---

## 6. Running Playbooks with Vault

When using playbooks that include vault-encrypted files, you must provide the vault password.

### Option 1: Ask for password
```bash
ansible-playbook site.yml --ask-vault-pass
```

### Option 2: Use a password file
```bash
ansible-playbook site.yml --vault-password-file ~/.vault_pass.txt
```

*(Make sure `~/.vault_pass.txt` has the vault password and is protected with proper permissions.)*

---

## 7. Encrypting Variables (Inline Encryption)

Instead of encrypting whole files, you can encrypt just a single variable using `ansible-vault encrypt_string`.

```bash
ansible-vault encrypt_string 'MySecretPassword' --name 'db_password'
```

**Output:**
```yaml
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          623364353961323236376361353234323561393233366265653166346265653...
```

You can paste this directly into a playbook or variable file.

---

## 8. Changing Vault Password

You can change the password of an encrypted file:

```bash
ansible-vault rekey secrets.yml
```

---

## 9. Multiple Vaults (Vault IDs)

You can use different vault passwords for different files by assigning **vault IDs**.

```bash
ansible-vault encrypt --vault-id dev@prompt dev-secrets.yml
ansible-vault encrypt --vault-id prod@prompt prod-secrets.yml
```

Run playbook with:
```bash
ansible-playbook site.yml --vault-id dev@prompt --vault-id prod@prompt
```

---

## 10. Example: Using Vault in Playbooks

**Encrypted file (`vault.yml`):**
```yaml
db_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          646633303730316433396132363234396335333333323937323232356564
```

**Playbook (`site.yml`):**
```yaml
- hosts: dbservers
  vars_files:
    - vault.yml
  tasks:
    - name: Print secret
      debug:
        msg: "Database password is {{ db_password }}"
```

---

# ✅ Summary

- **Ansible Vault** secures sensitive data.  
- You can **create, encrypt, decrypt, edit, view** vault files.  
- Supports **inline variable encryption** (`encrypt_string`).  
- Use **vault IDs** for managing multiple environments (dev, prod).  
- Run playbooks with `--ask-vault-pass` or `--vault-password-file`.  

Vault ensures your secrets remain **safe and encrypted**, even if your playbooks are stored in version control systems like Git.
