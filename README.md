# Network Attached Storage Server

A custom-built two-node NAS server cluster featuring RAID 5 redundancy, firewall protection, and over 5TB of fault-tolerant storage.

<img width="234" height="356" alt="image" src="https://github.com/user-attachments/assets/0712b3c1-ffa5-4c9a-a87c-14c9939d04ee" />

(images/primary-node-interior.png)
*Interior of the custom-built primary storage node with RGB cooling and RAID array*

---

## 🖥️ System Architecture

This NAS solution consists of two networked nodes working together to provide reliable, secure, and high-performance network storage.

```
┌─────────────────────────────────────────────────────────────────┐
│                        NETWORK                                  │
│                           │                                     │
│              ┌────────────┴────────────┐                        │
│              │                         │                        │
│     ┌────────▼────────┐       ┌────────▼────────┐               │
│     │  PRIMARY NODE   │       │ SECONDARY NODE  │               │
│     │  (Custom Build) │◄─────►│ (Dell OptiPlex) │               │
│     │                 │       │                 │               │
│     │  AMD Ryzen 5    │       │  Intel i5 9th   │               │
│     │  5+ TB RAID 5   │       │  256 GB SSD     │               │
│     │  + Firewall     │       │                 │               │
│     └─────────────────┘       └─────────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📋 Hardware Specifications

### Node 1: Primary Storage Server (Custom Build)

| Component | Specification |
|-----------|---------------|
| **CPU** | AMD Ryzen 5 7600 (6-core, 12-thread) |
| **Memory** | 16 GB DDR5 RAM |
| **Storage** | 5+ TB RAID 5 Array |
| **Redundancy** | RAID 5 (single drive fault tolerance) |
| **Network Security** | Hardware/Software Firewall |
| **Cooling** | RGB Case Fans |

### Node 2: Secondary Server (Dell OptiPlex Micro)

| Component | Specification |
|-----------|---------------|
| **CPU** | Intel Core i5 (9th Generation) |
| **Memory** | 16 GB DDR4 RAM |
| **Storage** | 256 GB SSD |
| **Form Factor** | Dell OptiPlex Micro |

---

## 🔒 Features

- **RAID 5 Redundancy** — Continues operating even if one drive fails, with automatic data recovery
- **Firewall Protection** — Network-level security to protect stored data from unauthorized access
- **Two-Node Architecture** — Distributed workload and backup capabilities
- **5+ TB Usable Storage** — Ample space for file storage, backups, and media
- **Low Power Secondary Node** — Dell OptiPlex Micro provides efficient always-on services

---

## 🛠️ Use Cases

- **Home Media Server** — Stream movies, music, and photos across your network
- **Automated Backups** — Centralized backup destination for all network devices
- **File Sharing** — SMB/NFS shares for seamless file access
- **Development Environment** — Host containers, VMs, or development tools
- **Personal Cloud** — Self-hosted alternative to cloud storage services

---

## 📁 Repository Structure

```
NetworkAttachedStorageServer/
├── config/                 # Configuration files
├── images/                 # Build photos and diagrams
│   └── primary-node-interior.png
├── scripts/                # Setup and maintenance scripts
├── docs/                   # Additional documentation
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Network switch or router
- Static IP addresses configured for both nodes
- NAS operating system (TrueNAS, OpenMediaVault, Unraid, etc.)

### Initial Setup

1. Connect both nodes to your network
2. Configure static IP addresses
3. Set up RAID 5 array on the primary node
4. Configure firewall rules
5. Set up shared folders and user permissions
6. Configure secondary node for desired services

---

## 📊 RAID 5 Configuration

The primary node uses RAID 5, which provides:

- **Fault Tolerance**: Survives single drive failure
- **Read Performance**: Improved read speeds through striping
- **Storage Efficiency**: ~75-80% usable capacity (with 4 drives)
- **Parity Distribution**: Distributed parity across all drives

> ⚠️ **Note**: RAID is not a backup. Always maintain off-site backups of critical data.

---

## 🔧 Maintenance

- **Monitor Drive Health**: Regularly check S.M.A.R.T. data
- **Test Rebuilds**: Periodically verify RAID rebuild capability
- **Update Firmware**: Keep drives and system firmware current
- **Review Firewall Logs**: Monitor for suspicious activity

---

## 📄 License

This project documentation is provided for educational and reference purposes.

---

## 🙏 Acknowledgments

Built with care for reliable home/small office network storage.
