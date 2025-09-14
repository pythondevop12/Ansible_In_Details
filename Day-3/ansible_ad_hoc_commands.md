# Ansible Ad-hoc Commands Cheat Sheet

Ad-hoc commands are **one-time commands** executed directly from the command line without writing a playbook.  
They are useful for quick tasks such as package installation, service management, file operations, and gathering system information.

---

## General Syntax
```bash
ansible <host-pattern> -m <module> -a "<module-options>" [-u <user>] [--become]
```

- **`<host-pattern>`** → group/host defined in the inventory (e.g., `all`, `webservers`)  
- **`-m`** → specifies the module (e.g., `ping`, `yum`, `apt`)  
- **`-a`** → arguments for the module  

---

## 1. Connectivity Test

### Ping all hosts
```bash
ansible all -m ping
```

---

## 2. Package Management

### Install package with `yum` (RHEL/CentOS/Amazon Linux)
```bash
ansible webservers -m yum -a "name=httpd state=present"
```

### Install package with `apt` (Debian/Ubuntu)
```bash
ansible webservers -m apt -a "name=nginx state=present update_cache=yes"
```

### Remove a package
```bash
ansible webservers -m yum -a "name=httpd state=absent"
```

### Upgrade all packages
```bash
ansible all -m apt -a "upgrade=dist"
```

---

## 3. Service Management

### Start a service
```bash
ansible webservers -m service -a "name=httpd state=started"
```

### Stop a service
```bash
ansible webservers -m service -a "name=httpd state=stopped"
```

### Restart a service
```bash
ansible webservers -m service -a "name=httpd state=restarted"
```

### Enable service at boot
```bash
ansible webservers -m service -a "name=httpd enabled=yes"
```

---

## 4. File & Directory Management

### Copy a file
```bash
ansible webservers -m copy -a "src=/etc/hosts dest=/tmp/hosts"
```

### Create a directory
```bash
ansible webservers -m file -a "path=/tmp/testdir state=directory"
```

### Remove a file
```bash
ansible webservers -m file -a "path=/tmp/oldfile.txt state=absent"
```

### Create a symlink
```bash
ansible webservers -m file -a "src=/usr/bin/python3 dest=/usr/bin/python state=link"
```

---

## 5. User & Group Management

### Create a user
```bash
ansible all -m user -a "name=devops state=present"
```

### Delete a user
```bash
ansible all -m user -a "name=devops state=absent remove=yes"
```

### Add user to a group
```bash
ansible all -m user -a "name=devops groups=wheel append=yes"
```

---

## 6. Command & Shell Execution

### Run a command
```bash
ansible all -m command -a "uptime"
```

### Run a shell command
```bash
ansible all -m shell -a "echo hello > /tmp/hello.txt"
```

### Run command with elevated privileges
```bash
ansible all -b -m command -a "systemctl restart sshd"
```

---

## 7. File Transfer & Fetch

### Fetch file from remote node to control machine
```bash
ansible webservers -m fetch -a "src=/var/log/messages dest=/tmp/ logs/"
```

---

## 8. System Information

### Gather all facts
```bash
ansible all -m setup
```

### Get only memory-related facts
```bash
ansible all -m setup -a 'filter=ansible_mem*'
```

---

## 9. Disk & File Permissions

### Change file permissions
```bash
ansible all -m file -a "path=/tmp/hello.txt mode=0644"
```

### Change file ownership
```bash
ansible all -m file -a "path=/tmp/hello.txt owner=root group=root"
```

---

## 10. Networking

### Copy SSH key to hosts
```bash
ansible all -m authorized_key -a "user=devops key='{{ lookup('file', '/home/devops/.ssh/id_rsa.pub') }}'"
```

### Manage firewall (example with ufw)
```bash
ansible all -m ufw -a "rule=allow port=22 proto=tcp"
```

---

# Summary
- **Ad-hoc commands** are for quick, one-time operations.  
- They help with **testing, troubleshooting, and immediate fixes**.  
- For repeatable tasks, **use Playbooks** instead.  

This cheat sheet covers the most frequently used **ad-hoc commands** for daily system administration and DevOps tasks.
