# Ansible Handlers – Complete Guide

## 📌 What are Handlers?
Handlers in Ansible are special tasks that run **only when notified** by another task.  
They are typically used to perform actions such as restarting a service after a configuration change.

👉 Think of handlers as **event-driven tasks**:
- If nothing triggers them → they don’t run.
- If multiple tasks trigger the same handler → it runs **only once** at the end of the play.

---

## 📌 Why use Handlers?
- To avoid unnecessary service restarts.
- To keep playbooks **idempotent** (safe to run multiple times).
- To separate **changes** from **reactions**.

---

## 📌 Handler Basics

### 1. Defining a Handler
Handlers are defined inside `handlers/main.yml` of a role, or in the playbook under `handlers:`.

Example:

```yaml
# handlers/main.yml
---
- name: Restart nginx
  ansible.builtin.service:
    name: nginx
    state: restarted
