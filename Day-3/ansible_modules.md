# Ansible Modules Guide

Ansible uses **modules** to perform specific tasks on managed nodes. Each module is like a small program that Ansible runs through playbooks or ad-hoc commands. Below is a detailed explanation of some commonly used modules.

---

## 1. `ping` Module
The `ping` module is used to test connectivity between the Ansible control node and managed nodes.  
It does not use ICMP ping, but instead verifies if Python is installed and Ansible can run commands.

### Example:
```bash
ansible all -m ping
```

**Output:**
```json
node1 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

---

## 2. `yum` Module (For RHEL/CentOS/Amazon Linux)
The `yum` module manages packages on Red Hat-based systems using the **YUM** package manager.

### Example: Install a package
```yaml
- name: Install httpd
  ansible.builtin.yum:
    name: httpd
    state: present
```

### Example: Remove a package
```yaml
- name: Remove httpd
  ansible.builtin.yum:
    name: httpd
    state: absent
```

---

## 3. `apt` Module (For Debian/Ubuntu)
The `apt` module manages packages on Debian-based systems using the **APT** package manager.

### Example: Install a package
```yaml
- name: Install nginx
  ansible.builtin.apt:
    name: nginx
    state: present
    update_cache: yes
```

### Example: Upgrade all packages
```yaml
- name: Upgrade all packages
  ansible.builtin.apt:
    upgrade: dist
```

---

## 4. `service` Module
The `service` module manages services (start, stop, restart, enable) on managed nodes.

### Example: Start a service
```yaml
- name: Start httpd service
  ansible.builtin.service:
    name: httpd
    state: started
```

### Example: Restart a service and enable it at boot
```yaml
- name: Restart nginx and enable
  ansible.builtin.service:
    name: nginx
    state: restarted
    enabled: yes
```

---

## 5. `copy` Module
The `copy` module copies files from the control node to managed nodes.

### Example: Copy a file
```yaml
- name: Copy configuration file
  ansible.builtin.copy:
    src: ./config.cfg
    dest: /etc/myapp/config.cfg
    owner: root
    group: root
    mode: '0644'
```

### Example: Copy inline content
```yaml
- name: Create a file with content
  ansible.builtin.copy:
    dest: /tmp/message.txt
    content: |
      Hello, this is managed by Ansible!
```

---

## 6. `file` Module
The `file` module is used to manage files, directories, and symlinks.

### Example: Create a directory
```yaml
- name: Create logs directory
  ansible.builtin.file:
    path: /var/log/myapp
    state: directory
    owner: myuser
    group: mygroup
    mode: '0755'
```

### Example: Remove a file
```yaml
- name: Remove a temp file
  ansible.builtin.file:
    path: /tmp/oldfile.txt
    state: absent
```

### Example: Create a symbolic link
```yaml
- name: Create symlink
  ansible.builtin.file:
    src: /usr/bin/python3
    dest: /usr/bin/python
    state: link
```

---

# Summary
- **ping** → Test connectivity  
- **yum** → Manage packages on RHEL/CentOS  
- **apt** → Manage packages on Debian/Ubuntu  
- **service** → Manage services  
- **copy** → Copy files from control node to managed node  
- **file** → Manage files, directories, and symlinks  

These modules form the backbone of day-to-day Ansible automation and are essential for configuration management and deployment.
