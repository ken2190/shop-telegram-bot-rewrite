# Misc buttons
try_again = "Try again."
skip = "⏭ Skip"
back = "🔙 back"
skip = "⏭ Skip"
tick = "✅"
cross = "❌"
yes = "✅ Yes"
no = "❌ No"
enabled = "✅ Enabled"
disabled = "❌ Disabled"
error = "An error has occurred!"
or_press_back = "or press the \"Back\" button."
or_press_skip = "or press the \"Skip\" button."
hide = "🙈 Hide"
show = "🐵 Show"
delete = "❌ Delete"
reset = "❌ Reset"
no_permission = "You do not have permission to execute this command!"
unknown_command = "I can't understand the command :("
cross = "❌"
too_many_categories = "Too many categories!"
unknown_call_stop_state = "The bot is waiting for your input, but you didn't enter anything. To exit the input mode, click the button below."
state_cancelled = "You have canceled the operation."
unknown_error = "An unknown error has occurred!"

# main markup
admin_panel = "🔴 Admin Panel"
faq = "ℹ️ FAQ"
profile = "📁 Profile"
catalog = "🗄️ Catalog"
cart = "🛒 Cart"
support_menu = "☎ Support Menu"

#cart
payment_method = "💳 Payment Method"
choose_payment_method = "Choose a payment method:"
def format_delivery(delivery_price: int) -> str:
     return f"🚚 Delivery: {delivery_price} rub."
delivery = "🚚 Delivery"
self_pickup = "🖐️ Pickup"
cart_empty = "Your cart is empty!"
def cart_total_price(price: float, currency_sym: str) -> str:
     return f"🛒 Final price: {price:.2f} {currency_sym}"

# Admin panel tabs
item_management = "📦 Item Management"
no_categories = "Create at least one category before creating a product!"
user_management = "🧍 User Management"
category_management = "📁 Categories"
stats = "📈 Statistics"
settings = "⚙ Settings"

# Main settings
language = "🌐 Language"
choose_a_language = f"Select language {or_press_skip}:"
language_was_set = "Language was successfully changed! Restart the bot to apply the changes."
english = "🇬🇧 English"
russian = "🇷🇺 Russian"
input_greeting = "Formatting: \n\"%s\" - username\n\nEnter a welcome message:"
greeting_was_set = "The welcome message has been successfully changed!"

greeting = "👋 Greeting"

#FAQ
contacts = "📞 Contacts"
refund_policy = "🎫 Refund Policy"

#Profile
my_orders = "📂 My Orders"
cancel_order = "❌ Cancel order"
restore_order = "✅ Restore order"
my_support_tickets = "🙋 My support tickets"
enable_notif = "🔔Enable order notifications"
disable_notif = "🔕Turn off order notifications"

# Catalog / Item / Cart
search = "🔍 Find"
add_to_cart = "🛒 Add to Cart"
not_in_stock = "❌ Out of Stock"
cart_is_empty = "Cart is empty."
category_is_empty = "Category is empty."
textpickup = "✅Pickup"
def delivery_on(price): return f"✅ Delivery - {price}rub."
def delivery_off(price): return f"❌ Delivery - {price}rub."
cart_checkout = "Checkout"
clear_cart = "Clear Cart"
status_processing = "Processing"
status_delivery = "Awaiting delivery"
status_done = "Ready"
status_cancelled = "Cancelled"
def item(item):
     stock = "custom" if item.is_custom else f"{item.amount}"
     return f"{item.name}\n{item.price:.2f} RUB\nStock: {stock}\n{item.description}"

# Category management
add_category = "🛍️ Add Category"
edit_category = "✏️ Edit category"
input_category_name = f"Enter category name {or_press_back}"
set_parent_category = f"📁 Select parent category {or_press_skip}"
category_created = "Category created successfully."
def format_category(category_id, category_name, category_parent_id, category_parent_name):
     return f"Category: [{category_id}]{category_name}\nParent category: {f'[{category_parent_id}]{category_parent_name}' if category_parent_id else 'None'}"
edit_parent_category = "📁 Edit Parent Category"
choose_a_category_to_edit = "Choose a category to edit:"
confirm_delete_category = "Are you sure you want to delete the category?"
category_deleted = "Category deleted successfully."

# Item management
def format_editItemsCategory_text(category_name: str) -> str:
     return f"Select a product to edit in the category {category_name}:"
add_item = "🗃️ Add Item"
edit_item = "✏️ Edit Item"

edit_name = "📋 Edit Name"
input_item_name = f"Enter product name {or_press_back}"

choose_category = "📁 Choose a category"
select_item_category = f"📁 Select product category {or_press_back}"
edit_category = "✏️ Edit category"

input_item_description = f"Enter product description {or_press_back}"
edit_description = "📝 Edit Description"

input_item_price = f"Enter item price {or_press_back}"
edit_price = "💰 Edit Price"
price_must_be_number = "Price must be a number."

send_item_images = f"🖼️ Send product image {or_press_skip}"
send_item_changed_images = f"🖼️ Send product image {or_press_back}"
delete_image = "❌ Delete Image"
edit_image = "🖼️ Edit Image"


confirm_delete_item = "Are you sure you want to delete the item?"
item_was_deleted = "Item was deleted successfully."
change_desc = "📝 Change Description"
change_price = "🏷️ Change Price"
change_item_cat = "🛍️ Change Category"
change_stock = "📦 Change Stock"
def format_confirm_item(name: str, description: str, category_id: int, price: float, images: list[str]) -> str:
     return f"Product: {name}\nDescription: {description}\nCategory: {category_id}\nPrice: {price}\nImage ID: {images}\n\nAre you sure you want to create a product?"
item_added = "Item added successfully."

# User management
user_does_not_exist = "User not found. {try_again}"
def format_user_profile(id: int, username: str, registration_date: str, is_admin: bool, is_manager: bool) -> str:
     role = "User"
     if is_admin:
         role = "Administrator"
     elif is_manager:
         role = "Manager"
     return f"ID: {id}\nName: {username}\nRegistration date: {registration_date}\nRole: {role}"
invalid_user_id = "Invalid user ID. {try_again}"

user_profile = "📁User Profile"
input_user_id = f"Enter user ID {or_press_back}"
notify_everyone = "🔔Notify all users"
input_notification = f"Enter alert text {or_press_back}"
def confirm_notification(text: str) -> str:
     return f"Are you sure you want to send an alert?\nText:\n{text}"
def notification_sent(done_users: int, total_users: int) -> str:
     return f"Alert successfully sent to {done_users}/{total_users} users."
orders = "📁 Orders"
remove_manager_role = "👨‍💼 Remove manager role"
add_manager_role = "👨‍💼 Make Manager"
remove_admin_role = "🔴 Remove admin role"
add_admin_role = "🔴 Make Admin"
def change_order_status(status): return f"Change status to \"{status}\""

# shop stats
registration_stats = "👥 Registration Statistics"
order_stats = "📦 Order Statistics"
all_time = "All time"
monthly = "Last 30 days"
weekly = "Last 7 days"
daily = "Last 24 hours"

# Payment settings
yoomoney = "🟢 YuMoney"
qiwi = "🏧 qiwi"



# shop settings
main_settings = "🛠️ Main Settings"
item_settings = "🗃️ Item Settings"
payment_settings = "💳 Payment Settings"
additional_settings = "📖 Additional Settings"
custom_commands = "📖 Commands"
add_command = "📝 Add Command"
clean_logs = "📖 Clean Logs"
clean_logs_text = "⚠️ Are you sure you want to clean the logs? They will be permanently deleted!\n(Today's logs will not be deleted)"
backups = "💾 Backup"
update_backup = "🔄 Update Backup"
load_backup = "💿 Load Backup"
clean_backups = "🧹 Cleanup Backups"
system_settings = "💻 System Settings"
clean_images = "🗑️ Delete Unused Images"
clean_images_text = "⚠️ Are you sure you want to delete unused images? They will be permanently deleted!"
clean_database = "📚 Clean Database"
clean_database_text = "⚠️ Are you sure you want to clean the database? All data will be permanently deleted!"
reset_settings = "⚙️ Reset Settings"
reset_settings_text = "⚠️ Are you sure you want to reset your settings? All data will be permanently deleted!"
image = "🖼️ Image"
checkout_settings = "🛒 Checkout Settings"
stats_settings = "📈 Statistics Settings"
graph_color = "🌈 Graph Color"
border_width = "🔲 Stroke Width"
title_font_size = "ℹ️ Graph title size"
axis_font_size = "↔️Axis text size"
tick_font_size = "🔢Tick Text Size"
unavailable = "⛔️"
minus="➖"
plus = "➕"
enable_sticker = "❌ Welcome Sticker"
disable_sticker = "✅ Welcome Sticker"

toggle_email = "Order Email"
toggle_phone_number = "Phone number when ordering"
enable_delivery = "❌ Delivery"
disable_delivery = "✅ Delivery"
toggle_captcha = "CAPTCHA on order"
enable_debug = "❌ Debug mode"

input_email = f"Enter email {or_press_back}"
input_phone = f"Enter phone number {or_press_back}"
input_address = f"Enter address {or_press_back}"
input_captcha = f"Enter CAPTCHA {or_press_back}"
input_captcha_error = "Invalid CAPTCHA"
input_email_error = "Invalid email"
input_phone_error = "Invalid phone number"

input_delivery_price = f"💰 Enter shipping cost {or_press_back}"
change_delivery_price = "💰 Change Shipping Price"
disable_debug = "✅ Debug Mode"

# Manager tab
view_order = "📂 View Order"

