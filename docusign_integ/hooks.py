app_name = "docusign_integ"
app_title = "docusign_integ"
app_publisher = "kenywod.a.c@gmail.com"
app_description = "Riverstone Custom Docusign App"
app_email = "kenywod.a.c@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/docusign_integ/css/docusign_integ.css"
# app_include_js = "/assets/docusign_integ/js/docusign_integ.js"

# include js, css files in header of web template
# web_include_css = "/assets/docusign_integ/css/docusign_integ.css"
# web_include_js = "/assets/docusign_integ/js/docusign_integ.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "docusign_integ/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "docusign_integ/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "docusign_integ.utils.jinja_methods",
# 	"filters": "docusign_integ.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "docusign_integ.install.before_install"
# after_install = "docusign_integ.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "docusign_integ.uninstall.before_uninstall"
# after_uninstall = "docusign_integ.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "docusign_integ.utils.before_app_install"
# after_app_install = "docusign_integ.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "docusign_integ.utils.before_app_uninstall"
# after_app_uninstall = "docusign_integ.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "docusign_integ.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"docusign_integ.tasks.all"
# 	],
# 	"daily": [
# 		"docusign_integ.tasks.daily"
# 	],
# 	"hourly": [
# 		"docusign_integ.tasks.hourly"
# 	],
# 	"weekly": [
# 		"docusign_integ.tasks.weekly"
# 	],
# 	"monthly": [
# 		"docusign_integ.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "docusign_integ.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "docusign_integ.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "docusign_integ.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["docusign_integ.utils.before_request"]
# after_request = ["docusign_integ.utils.after_request"]

# Job Events
# ----------
# before_job = ["docusign_integ.utils.before_job"]
# after_job = ["docusign_integ.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"docusign_integ.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

