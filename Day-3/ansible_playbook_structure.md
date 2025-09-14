# Ansible Playbook Structure

Ansible Playbooks are YAML files that define automation tasks.  
They contain instructions such as **which hosts to target, what tasks to run, variables to use, and privilege escalation**.  

This guide explains the **structure of a playbook** with focus on:  
- `hosts`  
- `tasks`  
- `vars`  
- `become`  

---

## 1. Basic Structure of a Playbook

A playbook is made of one or more **plays**.  
Each play defines a set of tasks to be executed on specific hosts.

### Example:
```yaml
- name: Basic Playbook Example
  hosts: webservers
  become: yes
  vars:
    package_name: nginx

  tasks:
    - name: Install a package
      apt:
        name: "{{ package_name }}"
        state: present

    - name: Start and enable service
      service:
        name: "{{ package_name }}"
        state: started
        enabled: yes
```

---

## 2. `hosts`

- Defines **which group or host(s)** in the inventory file the playbook should run against.
- Can be:
  - A group (e.g., `webservers`)
  - A single host (e.g., `192.168.1.10`)
  - `all` (all hosts in inventory)

### Example:
```yaml
hosts: webservers
```

---

## 3. `tasks`

- A list of **actions** Ansible should perform.
- Each task uses an **Ansible module** (like `apt`, `yum`, `service`, `copy`, etc.).
- Tasks are executed in order from top to bottom.

### Example:
```yaml
tasks:
  - name: Install nginx
    apt:
      name: nginx
      state: present

  - name: Start nginx service
    service:
      name: nginx
      state: started
```

---

## 4. `vars`

- Playbooks can define **variables** using the `vars` section.
- Variables make playbooks **dynamic and reusable**.
- Variables are referenced with Jinja2 syntax: `{{ variable_name }}`

### Example:
```yaml
vars:
  package_name: nginx
  service_state: started

tasks:
  - name: Install package
    apt:
      name: "{{ package_name }}"
      state: present

  - name: Manage service
    service:
      name: "{{ package_name }}"
      state: "{{ service_state }}"
```

---

## 5. `become`

- Used for **privilege escalation** (e.g., running tasks as `root`).
- Equivalent to using `sudo` in Linux.
- Can be set:
  - At play level → applies to all tasks
  - At task level → applies to specific tasks

### Example: Play level
```yaml
- name: Install nginx with privilege escalation
  hosts: webservers
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
```

### Example: Task level
```yaml
tasks:
  - name: Install nginx
    become: yes
    apt:
      name: nginx
      state: present
```

---

## 6. Complete Example Playbook

```yaml
- name: Configure Web Server
  hosts: webservers
  become: yes
  vars:
    package_name: nginx
    service_state: started

  tasks:
    - name: Install web server package
      apt:
        name: "{{ package_name }}"
        state: present
        update_cache: yes

    - name: Start and enable service
      service:
        name: "{{ package_name }}"
        state: "{{ service_state }}"
        enabled: yes
```

---

# ✅ Summary

- **hosts** → Defines target machines from inventory  
- **tasks** → Actions to perform (using Ansible modules)  
- **vars** → Variables for dynamic values  
- **become** → Privilege escalation (`sudo`)  

These four elements form the **core structure** of an Ansible playbook. Once you understand them, you can start building more complex automation with handlers, roles, and templates.
