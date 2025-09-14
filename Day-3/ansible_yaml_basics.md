# YAML Basics for Ansible

YAML (**YAML Ain’t Markup Language**) is the format used by Ansible for writing Playbooks, inventory files, and variables.  
It is designed to be **human-readable** and relies heavily on **indentation** to define structure.

This guide explains YAML basics with focus on **syntax and indentation**, so anyone can understand it.

---

## 1. Basic Rules of YAML
- YAML files use the `.yml` or `.yaml` extension.
- Indentation is done using **spaces only** (no tabs).
- Indentation defines **hierarchy** (parent-child relationships).
- Use **key-value pairs** for variables.
- Lists are written using a **dash (-)**.
- Comments start with `#`.

---

## 2. Key-Value Pairs

YAML represents data as **key: value**.

### Example:
```yaml
name: John Doe
age: 30
country: India
```

---

## 3. Indentation

Indentation shows nesting. Each level is indented with **2 spaces (recommended)**.

### Example:
```yaml
person:
  name: John
  age: 25
  address:
    city: Delhi
    pincode: 110001
```

Here:
- `person` is the parent key.
- `name`, `age`, `address` are children.
- Inside `address`, we have `city` and `pincode`.

---

## 4. Lists in YAML

Lists are created using a **dash (-)** followed by a space.

### Example: Simple list
```yaml
fruits:
  - apple
  - banana
  - orange
```

### Example: List of dictionaries
```yaml
users:
  - name: John
    role: admin
  - name: Alice
    role: developer
```

---

## 5. Dictionaries (Mappings)

Dictionaries are **key-value structures**.

### Example:
```yaml
server:
  hostname: web01
  ip: 192.168.1.10
  os: ubuntu
```

---

## 6. Boolean, Null, Numbers

YAML supports different data types.

### Example:
```yaml
enabled: true
debug: false
count: 5
price: 10.5
nothing: null
```

---

## 7. Strings

Strings can be written in plain text, single quotes, or double quotes.

```yaml
name1: John
name2: 'Alice'
name3: "Bob"
```

---

## 8. Multiline Strings

For long text, YAML supports block styles:
- **Literal block (|)** → preserves line breaks  
- **Folded block (>)** → joins lines into a single line

### Example:
```yaml
literal_block: |
  This is line one.
  This is line two.
  This will keep line breaks.

folded_block: >
  This is line one.
  This is line two.
  This will become a single line.
```

---

## 9. Comments

YAML supports comments with `#`.

```yaml
# This is a comment
app: myapp  # inline comment
```

---

## 10. YAML in Ansible

Ansible Playbooks are written in YAML format.

### Example Playbook:
```yaml
- name: Install and start nginx
  hosts: webservers
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Start nginx
      service:
        name: nginx
        state: started
```

---

# ✅ Summary

- **Indentation** is critical → use spaces, not tabs.  
- **Key-value pairs** define variables.  
- **Lists** use `-`.  
- **Dictionaries** use nested key-value pairs.  
- Supports **booleans, numbers, null, and strings**.  
- Ansible Playbooks = YAML files that define automation steps.  

Mastering **YAML basics** is the first step to writing effective **Ansible Playbooks**.
