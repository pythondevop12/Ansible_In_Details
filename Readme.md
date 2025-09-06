# Ansible Roadmap: Beginner to Advanced

This roadmap is designed to take you from **absolute beginner** to **advanced Ansible practitioner**. Follow step by step, practice along the way, and you'll gain strong hands-on knowledge.

---

## 1. **Introduction to Ansible (Beginner)**
- What is Ansible?
- Advantages of Ansible over other tools (Puppet, Chef, SaltStack)
- Key concepts:
  - Control node vs Managed nodes
  - Agentless architecture (SSH/WinRM based)
  - Declarative approach (idempotency)
- Installation & Setup:
  - Install Ansible on Linux/Mac/Windows (WSL)
  - Inventory basics (`/etc/ansible/hosts`)
  - Running first ad-hoc command (`ansible all -m ping`)

---

## 2. **Core Concepts**
- Inventory (Static vs Dynamic)
- Modules (e.g., `ping`, `yum`, `apt`, `service`, `copy`, `file`)
- Ad-hoc commands vs Playbooks
- YAML Basics (syntax, indentation)
- Configuration file (`ansible.cfg`)

---

## 3. **Playbooks (Beginner Level)**
- Structure of a Playbook:
  - `hosts`, `tasks`, `vars`, `become`
- Writing first playbook to:
  - Install packages
  - Copy files
  - Start/Stop services
- Handlers (restart service when config changes)
- Variables (inline, external vars files, group vars, host vars)

---

## 4. **Intermediate Playbook Features**
- Conditionals (`when`)
- Loops (`with_items`, `loop`)
- Templates (`.j2` Jinja2 templates)
- Tags (run specific parts of playbooks)
- Error handling (`ignore_errors`, `failed_when`, `rescue`, `always`)
- Blocks (group tasks together)

---

## 5. **Ansible Roles (Intermediate)**
- Role structure:
  ```
  roles/
    └── nginx/
        ├── tasks/
        ├── handlers/
        ├── templates/
        ├── vars/
        ├── defaults/
        └── meta/
  ```
- Creating and using roles
- Role dependencies
- Ansible Galaxy (`ansible-galaxy init`, `ansible-galaxy install`)

---

## 6. **Advanced Inventory Management**
- Grouping hosts (`[webservers]`, `[dbservers]`)
- Nested groups
- Dynamic inventory (AWS EC2, GCP, Azure plugins)
- Inventory scripts & plugins
- Variables precedence (host_vars, group_vars, CLI vars, facts)

---

## 7. **Ansible Advanced Playbook Features**
- Facts (`ansible_facts`)
- Register variables (`register` keyword)
- Delegation (`delegate_to`)
- Run tasks on localhost while managing remote nodes
- Ansible Vault (securing sensitive data like passwords/keys)
  - Encrypt & Decrypt files (`ansible-vault encrypt`)
  - Using vault in playbooks

---

## 8. **Jinja2 Templating (Intermediate to Advanced)**
- Variables, filters, and expressions
- Conditional templates
- Iterations inside templates
- Advanced filters (`default`, `to_json`, `from_yaml`, `regex_replace`)

---

## 9. **Error Handling & Debugging**
- `debug` module (printing variables)
- `assert` module
- Strategy plugins (`linear`, `free`)
- Ansible logs & verbose mode (`-v`, `-vvv`)

---

## 10. **Scaling Ansible (Advanced)**
- Using Ansible in CI/CD pipelines (Jenkins, GitLab, GitHub Actions)
- Ansible Tower / AWX:
  - RBAC
  - Scheduling jobs
  - Centralized logging
- Collections (reusable Ansible content)
- Custom modules & plugins (Python-based)

---

## 11. **Ansible with Cloud & Containers**
- Provisioning AWS, Azure, GCP resources
- Managing Docker containers & Kubernetes with Ansible
- Hybrid Infrastructure Automation

---

## 12. **Best Practices**
- Directory structure for projects
- Use of roles and collections
- Avoid hardcoding (always use variables)
- Use tags for selective execution
- Modular playbooks (include & import)
- Version control with Git

---

## 13. **Real-World Projects (Hands-On)**
- Configure Nginx/Apache web server cluster
- Deploy a database cluster (MySQL/PostgreSQL)
- Automate user management
- Provision AWS EC2 & configure security groups
- CI/CD pipeline automation with Ansible + Jenkins
- Kubernetes cluster bootstrap with Ansible

---

## 14. **Expert Level (Optional)**
- Writing custom Ansible modules (Python)
- Developing plugins (connection, lookup, filter)
- Contributing to Ansible Galaxy
- Performance tuning with forks and async tasks
- Large-scale inventory management

---

# ✅ Final Notes
- **Practice > Theory** → Run every concept on real servers (AWS free tier or local VMs).
- **Official Docs**: [https://docs.ansible.com](https://docs.ansible.com)
- **Community**: Join Ansible Slack & Reddit for real-world issues.

Happy Automating with Ansible 🚀
