# Vendor Management System

## Overview

The Vendor Management System is a Django-based web application that facilitates vendor management, purchase order tracking, and performance metric monitoring. This system comprises several modules, each serving a specific purpose.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Modules](#modules)
  - [Authentication](#authentication)
  - [Vendors](#vendors)
  - [Purchase Orders](#purchase-orders)
  - [Performance Tracking](#performance-tracking)
- [Requirements](#requirements)

## Installation

To set up the Vendor Management System, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd vendor-management-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the system through the provided URLs.
2. Obtain an authentication token by making a POST request to `/token/` with valid credentials.
3. Use the token to access protected endpoints, such as vendor creation (`/vendors/`) and purchase order management (`/purchase_orders/`).

## API Endpoints

### Authentication

- `/token/`: Obtain an authentication token.
- `/signup/`: Register a new user.

### Vendors

- `/vendors/`: List and create vendors.
- `/vendors/<int:id>/`: Retrieve, update, and delete a specific vendor.
- `/vendors/<int:id>/performance`: Retrieve the performance metrics of a specific vendor.

### Purchase Orders

- `/purchase_orders/`: List and create purchase orders.
- `/purchase_orders/<int:id>/`: Retrieve, update, and delete a specific purchase order.
- `/purchase_orders/<int:id>/acknowledge`: Acknowledge receipt of a purchase order.
- `/purchase_orders/<int:id>/delivered`: Mark a purchase order as delivered.
- `/purchase_orders/<int:id>/addrating`: Add a quality rating to a purchase order.

### Performance Tracking

- `/vendors/`: List and create vendors.
- `/vendors/<int:id>/performance`: Retrieve the performance metrics of a specific vendor.

## Modules

### Authentication

The system uses [Django SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/) for token-based authentication. The provided `MyTokenObtainPairView` allows users to obtain JWT tokens, and the `UserRegister` view enables user registration.

### Vendors

Manage vendors through the `VendorView` and `VendorDetailsView` classes. Retrieve vendor performance metrics with the `VendorPerformanceView`.

### Purchase Orders

Handle purchase orders using `PurchaseOrderView` for listing and creation, and `PurchaseOrderCRUDView` for retrieval, updating, and deletion. Acknowledge, deliver, and rate purchase orders using additional endpoints.

### Performance Tracking

Retrieve vendor performance metrics through the `VendorPerformanceView`.

## Requirements

The system requires the following dependencies, listed in the `requirements.txt` file.

If there is any concerns or feedback feel free to ask. - faizulafnaz22@gmail.com
