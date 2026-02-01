app_name = "pdf_a_3"
app_title = "Pdf A 3"
app_publisher = "ahmad900mohammad@gmail.com"
app_description = "pdf a3"
app_email = "ahmad900mohammad@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "pdf_a_3",
# 		"logo": "/assets/pdf_a_3/logo.png",
# 		"title": "Pdf A 3",
# 		"route": "/pdf_a_3",
# 		"has_permission": "pdf_a_3.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pdf_a_3/css/pdf_a_3.css"
# app_include_js = "/assets/pdf_a_3/js/pdf_a_3.js"

# include js, css files in header of web template
# web_include_css = "/assets/pdf_a_3/css/pdf_a_3.css"
# web_include_js = "/assets/pdf_a_3/js/pdf_a_3.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pdf_a_3/public/scss/website"

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
# app_include_icons = "pdf_a_3/public/icons.svg"

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
# 	"methods": "pdf_a_3.utils.jinja_methods",
# 	"filters": "pdf_a_3.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pdf_a_3.install.before_install"
# after_install = "pdf_a_3.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pdf_a_3.uninstall.before_uninstall"
# after_uninstall = "pdf_a_3.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "pdf_a_3.utils.before_app_install"
# after_app_install = "pdf_a_3.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "pdf_a_3.utils.before_app_uninstall"
# after_app_uninstall = "pdf_a_3.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pdf_a_3.notifications.get_notification_config"

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
# 		"pdf_a_3.tasks.all"
# 	],
# 	"daily": [
# 		"pdf_a_3.tasks.daily"
# 	],
# 	"hourly": [
# 		"pdf_a_3.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pdf_a_3.tasks.weekly"
# 	],
# 	"monthly": [
# 		"pdf_a_3.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "pdf_a_3.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pdf_a_3.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "pdf_a_3.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pdf_a_3.utils.before_request"]
# after_request = ["pdf_a_3.utils.after_request"]

# Job Events
# ----------
# before_job = ["pdf_a_3.utils.before_job"]
# after_job = ["pdf_a_3.utils.after_job"]

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
# 	"pdf_a_3.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

