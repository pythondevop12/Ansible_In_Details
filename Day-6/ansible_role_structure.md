# Ansible Role Structure

Roles in Ansible provide a way to **organize playbooks and reuse automation code**.  
Instead of writing large playbooks, you can split them into smaller components called **roles**.  

Each role has a standard directory structure with subfolders for tasks, handlers, variables, templates, and metadata.

---

## 1. Directory Structure of a Role

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
      └── meta/
           └── main.yml
```

---

## 2. Explanation of Each Directory

### **1. tasks/**
- Contains the list of tasks to be executed.  
- The entry point is `main.yml`.  
- Tasks usually include installing packages, configuring services, etc.  

**Example (`roles/nginx/tasks/main.yml`):**
```yaml
- name: Install nginx
  apt:
    name: nginx
    state: present
    update_cache: yes

- name: Copy nginx config
  template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
```

---

### **2. handlers/**
- Handlers are special tasks triggered by `notify` in other tasks.  
- Commonly used for restarting services after configuration changes.  

**Example (`roles/nginx/handlers/main.yml`):**
```yaml
- name: restart nginx
  service:
    name: nginx
    state: restarted
```

---

### **3. templates/**
- Contains **Jinja2 template files**.  
- Templates allow dynamic configuration files by using variables.  

**Example (`roles/nginx/templates/index.html.j2`):**
```html
<html>
  <head><title>{{ server_name }}</title></head>
  <body>
    <h1>Welcome to {{ server_name }}!</h1>
  </body>
</html>
```

---

### **4. vars/**
- Stores variables specific to the role.  
- Higher precedence than `defaults/`.  
- Use for values that rarely change.  

**Example (`roles/nginx/vars/main.yml`):**
```yaml
nginx_port: 80
server_name: myserver.local
```

---

### **5. defaults/**
- Contains default variables for the role.  
- Lowest precedence (can be overridden easily).  
- Use for values that can be overridden by the user.  

**Example (`roles/nginx/defaults/main.yml`):**
```yaml
nginx_port: 8080
```

---

### **6. meta/**
- Defines metadata about the role.  
- Can specify dependencies (other roles that should run before this one).  

**Example (`roles/nginx/meta/main.yml`):**
```yaml
---
dependencies:
  - role: common
```

---

## 3. Using the Role in a Playbook

After creating the role structure, you can include it in a playbook:

**Example (`site.yml`):**
```yaml
- name: Configure Nginx Web Server
  hosts: webservers
  become: yes
  roles:
    - nginx
```

---

# ✅ Summary

- `tasks/` → Main list of tasks to run  
- `handlers/` → Special tasks triggered by notifications  
- `templates/` → Jinja2 template files  
- `vars/` → Role-specific variables (high precedence)  
- `defaults/` → Default variables (low precedence, easy to override)  
- `meta/` → Role metadata and dependencies  

Roles help make playbooks **modular, reusable, and easy to maintain**.
