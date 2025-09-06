
# 📘 Ansible Inventory (Static vs Dynamic)

In Ansible, an **inventory** is a file that defines the hosts and groups of hosts on which Ansible will run tasks. It tells Ansible *“where”* to run playbooks.

There are two main types of inventories:
1. **Static Inventory**
2. **Dynamic Inventory**

---

## 🔹 1. Static Inventory

### ✅ Definition:
A **static inventory** is a simple text (INI, YAML, or JSON) file that lists servers (hosts) and organizes them into groups.

It is the most commonly used and straightforward way to manage inventories.

### 📄 Example (INI format):
```ini
[web]
webserver1 ansible_host=192.168.1.10 ansible_user=ubuntu
webserver2 ansible_host=192.168.1.11 ansible_user=ubuntu

[db]
dbserver1 ansible_host=192.168.1.20 ansible_user=ec2-user

[all:vars]
ansible_ssh_private_key_file=~/.ssh/id_rsa
ansible_python_interpreter=/usr/bin/python3
```

### 📄 Example (YAML format):
```yaml
all:
  vars:
    ansible_ssh_private_key_file: ~/.ssh/id_rsa
    ansible_python_interpreter: /usr/bin/python3
  children:
    web:
      hosts:
        webserver1:
          ansible_host: 192.168.1.10
          ansible_user: ubuntu
        webserver2:
          ansible_host: 192.168.1.11
          ansible_user: ubuntu
    db:
      hosts:
        dbserver1:
          ansible_host: 192.168.1.20
          ansible_user: ec2-user
```

### 🔑 Key Points:
- Easy to write and manage for small environments.
- Best suited for static or non-changing infrastructure.
- Useful for testing or small-scale automation.

---

## 🔹 2. Dynamic Inventory

### ✅ Definition:
A **dynamic inventory** allows Ansible to pull host information from external sources (like AWS, GCP, Azure, VMware, Kubernetes, or custom scripts).

It’s **dynamic** because it automatically updates when the infrastructure changes.

### 📄 Example: AWS EC2 Dynamic Inventory
```bash
ansible-inventory -i aws_ec2.yml --list
```

`aws_ec2.yml` (plugin configuration file):
```yaml
plugin: aws_ec2
regions:
  - us-east-1
  - us-west-2
filters:
  tag:Environment: dev
keyed_groups:
  - key: tags.Name
    prefix: instance
```

This will fetch all EC2 instances in the specified AWS regions and group them based on tags.

### 📄 Example: GCP Dynamic Inventory
```yaml
plugin: gcp_compute
projects:
  - my-gcp-project
zones:
  - us-central1-a
auth_kind: serviceaccount
service_account_file: /path/to/key.json
```

### 📄 Example: Using a Script
You can write a custom script (Python/JSON) that outputs inventory data.

Example (inventory.py):
```python
#!/usr/bin/env python3
import json

inventory = {
    "web": {
        "hosts": ["192.168.1.10", "192.168.1.11"]
    },
    "db": {
        "hosts": ["192.168.1.20"]
    }
}

print(json.dumps(inventory))
```

Make it executable and run:
```bash
ansible-inventory -i inventory.py --list
```

### 🔑 Key Points:
- Automatically discovers infrastructure.
- Best for **cloud-native** or **containerized** environments.
- Requires proper credentials and configuration.
- Scales easily for large environments.

---

## 🔹 Static vs Dynamic Inventory (Comparison)

| Feature                     | Static Inventory | Dynamic Inventory |
|------------------------------|-----------------|------------------|
| **Setup**                   | Simple, manual  | Requires plugins/API |
| **Best suited for**          | Small, stable infra | Cloud / large-scale infra |
| **Host updates**             | Manual changes | Auto-discovered |
| **Format**                   | INI, YAML, JSON | Plugins (YAML/JSON), scripts |
| **Complexity**               | Low             | Medium to High |
| **Scalability**              | Limited         | Highly scalable |

---

## 🔹 When to Use What?
- ✅ Use **Static Inventory** if you have a small, stable set of servers (like on-premises or testing environments).
- ✅ Use **Dynamic Inventory** if you’re working with **cloud providers** or **auto-scaling** infrastructure.

---

## 🚀 Summary
- Ansible inventory defines the hosts where automation runs.
- **Static inventory** is simple and manual.
- **Dynamic inventory** is powerful, automated, and integrates with cloud providers.
- Choose based on your infrastructure size and dynamic needs.

---

📌 With this knowledge, you can manage both small on-premises setups and large-scale cloud environments effectively.
