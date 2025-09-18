# Ansible Roles Guide

Ansible **roles** are a way to organize playbooks into reusable, modular components.  
Instead of writing everything in one large playbook, roles help structure automation into smaller, logical parts.

---

## 1. What is a Role?

- A **role** is a collection of tasks, variables, files, templates, and handlers organized in a standard directory structure.  
- Roles make playbooks **modular, reusable, and easy to maintain**.  
- Roles are usually stored inside a `roles/` directory.

---

## 2. Role Directory Structure

A typical role structure looks like this:

```
roles/
  └── nginx/
      ├── tasks/
      │    └── main.yml
      ├── handlers/
      │    └── main.yml
      ├── templates/
      │    └── index.html.j2
      ├── vars/
      │    └── main.yml
      ├── defaults/
      │    └── main.yml
      ├── files/
      │    └── example.conf
      └── meta/
           └── main.yml
```

---

## 3. Explanation of Role Components

### **1. tasks/**
- Contains the list of tasks (`main.yml`) to run for this role.  
- Tasks usually include installing packages, configuring services, etc.

```yaml
# roles/nginx/tasks/main.yml
- name: Install nginx
  apt:
    name: nginx
    state: present
    update_cache: yes
```

---

### **2. handlers/**
- Handlers are special tasks that run only when notified.  
- Commonly used for restarting services after a configuration change.

```yaml
# roles/nginx/handlers/main.yml
- name: restart nginx
  service:
    name: nginx
    state: restarted
```

---

### **3. templates/**
- Stores Jinja2 templates (`.j2` files).  
- Templates allow creating dynamic configuration files.

```html
<!-- roles/nginx/templates/index.html.j2 -->
<html>
  <body>
    <h1>Welcome to {{ server_name }}!</h1>
  </body>
</html>
```

---

### **4. vars/**
- Stores variables for the role (`main.yml`).  
- These variables have **higher precedence** than defaults.

```yaml
# roles/nginx/vars/main.yml
nginx_port: 80
server_name: myserver.local
```

---

### **5. defaults/**
- Stores default variables (`main.yml`).  
- Lowest precedence, can be easily overridden.  

```yaml
# roles/nginx/defaults/main.yml
nginx_port: 8080
```

---

### **6. files/**
- Contains static files that can be copied to hosts.  

```yaml
# Example task to copy file
- name: Copy config file
  copy:
    src: example.conf
    dest: /etc/nginx/example.conf
```

---

### **7. meta/**
- Stores metadata about the role.  
- Can define **dependencies** (roles that should run before this one).  

```yaml
# roles/nginx/meta/main.yml
---
dependencies:
  - role: common
```

---

## 4. Using Roles in Playbooks

Once the role is created, include it in a playbook:

```yaml
- name: Configure Web Servers
  hosts: webservers
  become: yes
  roles:
    - nginx
```

---

## 5. Creating Roles with Ansible Galaxy

You can use Ansible Galaxy to create a role structure automatically:

```bash
ansible-galaxy init nginx
```

This creates all required folders (`tasks/`, `handlers/`, `vars/`, etc.).

---

# ✅ Summary

- **Roles** organize automation into reusable components.  
- Standard role directories:  
  - `tasks/` → Main tasks  
  - `handlers/` → Special tasks (restart, reload, etc.)  
  - `templates/` → Jinja2 templates  
  - `vars/` → Role variables (higher precedence)  
  - `defaults/` → Default variables (lower precedence)  
  - `files/` → Static files  
  - `meta/` → Role dependencies  

Using roles makes playbooks **clean, reusable, and scalable**.
