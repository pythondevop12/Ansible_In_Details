
# 📘 Ansible Modules (ping, yum, apt, service, copy, file)

In Ansible, **modules** are small programs that perform a specific task.  
When you run a playbook or ad-hoc command, Ansible calls modules to execute the work on target hosts.

Some of the most commonly used modules are:

1. **ping**
2. **yum**
3. **apt**
4. **service**
5. **copy**
6. **file**

---

## 🔹 1. `ping` Module

### ✅ Purpose:
- Used to test the connection between Ansible control node and managed nodes.
- Verifies if the target machine is reachable and Python is available.

### 📄 Example:
```bash
ansible all -m ping
```

### 📄 Example in Playbook:
```yaml
- name: Test connection with hosts
  hosts: all
  tasks:
    - name: Ping all hosts
      ansible.builtin.ping:
```

### 🔑 Key Points:
- Does not use ICMP ping, but checks Python availability on the node.
- Useful for connectivity testing.

---

## 🔹 2. `yum` Module

### ✅ Purpose:
- Manages packages on **RHEL/CentOS/Fedora** systems using the `yum` package manager.

### 📄 Example: Install a package
```yaml
- name: Install httpd on CentOS
  hosts: web
  tasks:
    - name: Ensure httpd is installed
      ansible.builtin.yum:
        name: httpd
        state: present
```

### 📄 Example: Remove a package
```yaml
- name: Remove httpd
  hosts: web
  tasks:
    - name: Ensure httpd is removed
      ansible.builtin.yum:
        name: httpd
        state: absent
```

### 🔑 Key Points:
- Works only on RHEL-based distributions.
- `state: present` → installs package, `absent` → removes package, `latest` → upgrades package.

---

## 🔹 3. `apt` Module

### ✅ Purpose:
- Manages packages on **Debian/Ubuntu** systems using the `apt` package manager.

### 📄 Example: Install a package
```yaml
- name: Install nginx on Ubuntu
  hosts: web
  tasks:
    - name: Ensure nginx is installed
      ansible.builtin.apt:
        name: nginx
        state: present
        update_cache: yes
```

### 📄 Example: Upgrade all packages
```yaml
- name: Upgrade all packages
  hosts: all
  tasks:
    - name: Update all installed packages
      ansible.builtin.apt:
        upgrade: dist
```

### 🔑 Key Points:
- Works only on Debian-based distributions.
- Use `update_cache: yes` to update package index before installing.

---

## 🔹 4. `service` Module

### ✅ Purpose:
- Manages services (start, stop, restart, enable/disable).

### 📄 Example:
```yaml
- name: Manage services
  hosts: web
  tasks:
    - name: Start and enable httpd
      ansible.builtin.service:
        name: httpd
        state: started
        enabled: yes
```

### 📄 Another Example:
```yaml
- name: Restart nginx service
  hosts: web
  tasks:
    - name: Restart nginx
      ansible.builtin.service:
        name: nginx
        state: restarted
```

### 🔑 Key Points:
- Works across Linux distributions.
- `state:` values → `started`, `stopped`, `restarted`, `reloaded`.

---

## 🔹 5. `copy` Module

### ✅ Purpose:
- Copies files from the Ansible control node to managed nodes.

### 📄 Example:
```yaml
- name: Copy configuration file
  hosts: all
  tasks:
    - name: Copy nginx.conf to servers
      ansible.builtin.copy:
        src: /home/ansible/nginx.conf
        dest: /etc/nginx/nginx.conf
        owner: root
        group: root
        mode: '0644'
```

### 📄 Example with inline content:
```yaml
- name: Create a text file
  hosts: all
  tasks:
    - name: Write content into file
      ansible.builtin.copy:
        dest: /tmp/hello.txt
        content: |
          Hello, this is Ansible copy module example.
```

### 🔑 Key Points:
- `src` must be available on the control node.
- Can also create files with `content:`.

---

## 🔹 6. `file` Module

### ✅ Purpose:
- Used to manage file **attributes** (permissions, ownership, symbolic links, directories).

### 📄 Example: Create a directory
```yaml
- name: Create a directory
  hosts: all
  tasks:
    - name: Create logs directory
      ansible.builtin.file:
        path: /var/log/myapp
        state: directory
        owner: root
        group: root
        mode: '0755'
```

### 📄 Example: Remove a file
```yaml
- name: Remove a file
  hosts: all
  tasks:
    - name: Delete old log file
      ansible.builtin.file:
        path: /tmp/old.log
        state: absent
```

### 📄 Example: Create a symlink
```yaml
- name: Create symbolic link
  hosts: all
  tasks:
    - name: Link /var/log/app.log to /tmp/app.log
      ansible.builtin.file:
        src: /tmp/app.log
        dest: /var/log/app.log
        state: link
```

### 🔑 Key Points:
- `state: directory` → create directory
- `state: touch` → create empty file
- `state: absent` → remove file/directory
- `state: link` → create symlink

---

## 🚀 Summary

| Module   | Purpose |
|----------|---------|
| **ping** | Test connectivity with hosts |
| **yum**  | Manage packages on RHEL/CentOS/Fedora |
| **apt**  | Manage packages on Debian/Ubuntu |
| **service** | Start/stop/restart services |
| **copy** | Copy files or create files with content |
| **file** | Manage file attributes (permissions, directories, symlinks) |

---

📌 With these modules, you can manage connectivity, install software, handle services, and manage files across your infrastructure effectively.
