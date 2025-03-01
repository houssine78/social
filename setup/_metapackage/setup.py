import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-social",
    description="Meta package for oca-social Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-base_search_mail_content',
        'odoo14-addon-email_template_qweb',
        'odoo14-addon-mail_activity_board',
        'odoo14-addon-mail_allow_portal_internal_note',
        'odoo14-addon-mail_attach_existing_attachment',
        'odoo14-addon-mail_autosubscribe',
        'odoo14-addon-mail_debrand',
        'odoo14-addon-mail_inline_css',
        'odoo14-addon-mail_layout_preview',
        'odoo14-addon-mail_notification_custom_subject',
        'odoo14-addon-mail_outbound_static',
        'odoo14-addon-mail_preview_base',
        'odoo14-addon-mail_restrict_send_button',
        'odoo14-addon-mail_send_copy',
        'odoo14-addon-mail_tracking',
        'odoo14-addon-mail_tracking_mailgun',
        'odoo14-addon-mail_tracking_mass_mailing',
        'odoo14-addon-mass_mailing_contact_partner',
        'odoo14-addon-mass_mailing_custom_unsubscribe',
        'odoo14-addon-mass_mailing_event_registration_exclude',
        'odoo14-addon-mass_mailing_list_dynamic',
        'odoo14-addon-mass_mailing_partner',
        'odoo14-addon-mass_mailing_resend',
        'odoo14-addon-mass_mailing_subscription_date',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
