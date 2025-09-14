# Ansible Configuration File (`ansible.cfg`)

The `ansible.cfg` file is the main configuration file for Ansible.  
It allows you to define default settings for how Ansible behaves when running commands, playbooks, or modules.

This guide explains the **location, structure, and important parameters** of `ansible.cfg` in detail.

---

## 1. Locations of `ansible.cfg`

Ansible looks for the configuration file in the following order (first found is used):

1. **ANSIBLE_CONFIG** → Environment variable (highest priority)
2. `ansible.cfg` → In the current working directory
3. `~/.ansible.cfg` → In the user’s home directory
4. `/etc/ansible/ansible.cfg` → System-wide default (lowest priority)

👉 This means you can override system defaults by placing your own `ansible.cfg` in your project directory.

---

## 2. Basic Structure of `ansible.cfg`

The configuration file uses **INI format** with sections like `[defaults]`, `[privilege_escalation]`, `[ssh_connection]`.

### Example `ansible.cfg`
```ini
[defaults]
inventory      = ./inventory
remote_user    = ansible
host_key_checking = False
retry_files_enabled = False
roles_path     = ./roles

[privilege_escalation]
become          = True
become_method   = sudo
become_user     = root
become_ask_pass = False

[ssh_connection]
ssh_args = -o ControlMaster=auto -o ControlPersist=60s
```

---

## 3. Important Sections and Parameters

### **[defaults] Section**
Defines general settings.

| Parameter             | Description |
|------------------------|-------------|
| `inventory`            | Path to inventory file (default: `/etc/ansible/hosts`) |
| `remote_user`          | Default user to connect with |
| `host_key_checking`    | If `False`, skips SSH key verification |
| `roles_path`           | Path to roles directory |
| `retry_files_enabled`  | If `False`, disables creation of retry files |
| `timeout`              | Timeout for SSH connections |

---

### **[privilege_escalation] Section**
Controls how privilege escalation works.

| Parameter             | Description |
|------------------------|-------------|
| `become`              | Enable privilege escalation (True/False) |
| `become_method`       | Method to use (`sudo`, `su`, `pbrun`, etc.) |
| `become_user`         | User to switch to (default: root) |
| `become_ask_pass`     | Whether to prompt for password |

---

### **[ssh_connection] Section**
Controls SSH-related options.

| Parameter             | Description |
|------------------------|-------------|
| `ssh_args`            | Extra SSH arguments |
| `control_path`        | Location of SSH control socket |
| `pipelining`          | Enables pipelining to reduce SSH operations |

---

### **[paramiko_connection] Section**
Settings when using **Paramiko** (instead of OpenSSH).

| Parameter             | Description |
|------------------------|-------------|
| `record_host_keys`    | Record SSH host keys automatically |

---

## 4. Example Custom `ansible.cfg`

```ini
[defaults]
inventory      = ./hosts
remote_user    = ubuntu
private_key_file = ~/.ssh/id_rsa
host_key_checking = False
retry_files_enabled = False

[privilege_escalation]
become          = True
become_method   = sudo
become_user     = root

[ssh_connection]
pipelining = True
ssh_args = -o StrictHostKeyChecking=no
```

---

## 5. How to Check Active Configuration

You can see which config file Ansible is using with:

```bash
ansible --version
```

**Example Output:**
```
ansible [core 2.16.0]
  config file = /home/user/project/ansible.cfg
  configured module search path = ['/home/user/.ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.10/site-packages/ansible
  ansible collection location = /home/user/.ansible/collections:/usr/share/ansible/collections
```

---

# ✅ Summary

- `ansible.cfg` defines **global and project-specific settings**.  
- Search order: **Environment > Project > Home > System-wide**.  
- Key sections:
  - `[defaults]` → inventory, user, roles, retry files  
  - `[privilege_escalation]` → sudo/become settings  
  - `[ssh_connection]` → SSH optimizations  

Having a proper `ansible.cfg` makes your automation **faster, consistent, and easier to manage**.
