# Lead Conversion Control

A Frappe app to control lead conversion options in ERPNext.

## Features

- Control which lead conversion options are available (Customer, Opportunity, Quotation, Prospect)
- Global settings through the "Lead Conversion Settings" DocType
- Seamless integration with ERPNext's Lead form

## Installation

### Local Development

1. Get Frappe Framework: [https://frappeframework.com/docs/v14/user/en/installation](https://frappeframework.com/docs/v14/user/en/installation)
2. Once Frappe is installed, add this app to your bench:

```bash
bench get-app https://github.com/YOUR_USERNAME/lead_conversion_control
bench --site your-site.local install-app lead_conversion_control
```

### Frappe Cloud Installation

1. Go to your site on Frappe Cloud
2. Under "Apps", click "Install Custom App"
3. Enter the GitHub repository URL
4. Click Install

## Configuration

1. After installation, go to "Lead Conversion Settings" in ERPNext
2. Enable/disable the main "Allow Lead Conversion" toggle
3. Configure which conversion options should be available

## License

MIT