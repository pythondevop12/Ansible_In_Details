# Ansible Variables Guide

Variables in Ansible make playbooks **flexible, reusable, and dynamic**.  
They allow you to store values (like package names, paths, ports) and use them across playbooks, roles, and tasks.

---

## 1. What are Variables in Ansible?

- Variables are **key-value pairs**.
- Values can be strings, numbers, lists, or dictionaries.
- Variables are referenced using **Jinja2 syntax**:  
  ```yaml
  {{ variable_name }}
  ```

---

## 2. Defining Variables

### Inline Variables
Defined directly inside a playbook under `vars`.

```yaml
- hosts: webservers
  vars:
    package_name: nginx
    service_name: nginx

  tasks:
    - name: Install package
      apt:
        name: "{{ package_name }}"
        state: present

    - name: Start service
      service:
        name: "{{ service_name }}"
        state: started
```

---

### In a Separate File
Variables can be stored in a separate file and included in playbooks.

**`vars.yml`:**
```yaml
package_name: nginx
service_name: nginx
```

**Playbook:**
```yaml
- hosts: webservers
  vars_files:
    - vars.yml
  tasks:
    - name: Install package
      apt:
        name: "{{ package_name }}"
        state: present
```

---

### Role Variables

- `defaults/main.yml` → Default variables (lowest precedence, easy to override).  
- `vars/main.yml` → Role-specific variables (higher precedence, rarely overridden).  

---

## 3. Types of Variables

### Strings
```yaml
app_name: "myapp"
```

### Numbers
```yaml
max_retries: 5
```

### Boolean
```yaml
debug_mode: true
```

### Lists
```yaml
packages:
  - nginx
  - git
  - curl
```

### Dictionaries
```yaml
user_info:
  name: devops
  uid: 1001
  shell: /bin/bash
```

---

## 4. Variable Precedence

If the same variable is defined in multiple places, Ansible follows a **precedence order**.  
From **lowest** to **highest** priority:

1. Role defaults (`defaults/main.yml`)
2. Inventory file/group vars
3. Playbook `vars`
4. Extra vars (`--extra-vars` in command line)

👉 **Extra vars always win!**

---

## 5. Registering Variables

You can **capture command/module output** into variables using `register`.

```yaml
- name: Check uptime
  command: uptime
  register: uptime_output

- name: Print uptime
  debug:
    var: uptime_output.stdout
```

---

## 6. Facts as Variables

Ansible automatically gathers system facts and makes them available as variables.

```yaml
- name: Show OS distribution
  debug:
    var: ansible_distribution
```

Example values:
- `ansible_hostname`
- `ansible_all_ipv4_addresses`
- `ansible_os_family`

---

## 7. Using Variables in Templates

You can use variables inside Jinja2 templates (`.j2` files).

**Template (`index.html.j2`):**
```html
<html>
  <body>
    <h1>Welcome to {{ app_name }} running on port {{ app_port }}</h1>
  </body>
</html>
```

---

## 8. Overriding Variables with Extra Vars

You can override variables at runtime using `--extra-vars`.

```bash
ansible-playbook site.yml --extra-vars "app_port=8080"
```

---

# ✅ Summary

- Variables store reusable values.  
- Can be defined in **playbooks, inventory, variable files, or roles**.  
- Types: string, number, boolean, list, dictionary.  
- Precedence matters → **extra-vars > play vars > role vars > defaults**.  
- Registered variables capture output of tasks.  
- Facts are built-in system variables.  

Variables make Ansible playbooks **dynamic, configurable, and powerful**.
