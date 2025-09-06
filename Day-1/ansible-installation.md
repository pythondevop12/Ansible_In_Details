# Ansible Installation & Setup Guide

This guide will walk you through the installation and basic setup of
**Ansible** on different platforms, along with inventory basics and
running your first ad-hoc command.

------------------------------------------------------------------------

## 1. Installing Ansible

### 1.1 Install Ansible on Linux

Most Linux distributions provide Ansible via package managers.

**On Ubuntu/Debian:**

``` bash
sudo apt update
sudo apt install ansible -y
```

**On CentOS/RHEL (using EPEL repo):**

``` bash
sudo yum install epel-release -y
sudo yum install ansible -y
```

**On Fedora:**

``` bash
sudo dnf install ansible -y
```

You can verify installation with:

``` bash
ansible --version
```

------------------------------------------------------------------------

### 1.2 Install Ansible on MacOS

On MacOS, the easiest way is using **Homebrew**.

``` bash
brew install ansible
```

Verify installation:

``` bash
ansible --version
```

------------------------------------------------------------------------

### 1.3 Install Ansible on Windows (using WSL)

Since Ansible does not run natively on Windows, we use **Windows
Subsystem for Linux (WSL)**.

1.  Enable **WSL** feature on Windows:

    ``` powershell
    wsl --install
    ```

2.  Install a Linux distribution (like Ubuntu) from the Microsoft Store.

3.  Open Ubuntu (from Start Menu) and install Ansible:

    ``` bash
    sudo apt update
    sudo apt install ansible -y
    ```

4.  Check installation:

    ``` bash
    ansible --version
    ```

------------------------------------------------------------------------

## 2. Inventory Basics

Ansible uses an **inventory file** to define which hosts it will manage.

Default location: `/etc/ansible/hosts`

Example inventory file:

``` ini
[webservers]
192.168.1.10
192.168.1.11

[dbservers]
db1.example.com
db2.example.com
```

You can also use host variables:

``` ini
[webservers]
192.168.1.10 ansible_user=ubuntu ansible_port=22
192.168.1.11 ansible_user=ec2-user
```

To use a custom inventory file, run:

``` bash
ansible -i inventory.ini all -m ping
```

------------------------------------------------------------------------

## 3. Running First Ad-Hoc Command

Once Ansible is installed and the inventory file is configured, you can
test connectivity with the `ping` module.

### 3.1 Ping All Hosts

``` bash
ansible all -m ping
```

Expected output:

``` json
192.168.1.10 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.1.11 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

### 3.2 Running a Command

``` bash
ansible all -m command -a "uptime"
```

This will show the uptime of all managed hosts.

------------------------------------------------------------------------

## Summary

-   Installed Ansible on Linux, MacOS, and Windows (via WSL).
-   Learned about inventory basics (`/etc/ansible/hosts`).
-   Ran the first Ansible ad-hoc command (`ansible all -m ping`).

You are now ready to start writing **Ansible Playbooks**!
