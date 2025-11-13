<!-- GENERATED:MODULE -->
---
tags: [odoo, v19, community, module]
---

# Website

- Version: v19
- Category: community
- Source: odoo19/addons/website
- Dependencies: [[Odoo 19/Community Addons/digest/digest|digest]], [[Odoo 19/Community Addons/web/web|web]], [[Odoo 19/Community Addons/html_editor/html_editor|html_editor]], [[Odoo 19/Community Addons/http_routing/http_routing|http_routing]], [[Odoo 19/Community Addons/portal/portal|portal]], [[Odoo 19/Community Addons/social_media/social_media|social_media]], [[Odoo 19/Community Addons/auth_signup/auth_signup|auth_signup]], [[Odoo 19/Community Addons/mail/mail|mail]], [[Odoo 19/Community Addons/google_recaptcha/google_recaptcha|google_recaptcha]], [[Odoo 19/Community Addons/utm/utm|utm]], [[Odoo 19/Community Addons/html_builder/html_builder|html_builder]]

## Summary

Enterprise website builder

## XML Artifacts (detected)

- Views: 54
- Actions: 24
- Menus: 24
- Rules (ir.rule): 8
- Access CSV entries: 44

## Detected Models

- `IrActionsServer`
- `IrAsset`
- `IrAttachment`
- `IrModelData`
- `ir.module.module`
- `IrRule`
- `IrUiMenu`
- `ir.ui.view`
- `ResCompany`
- `ResLang`
- `res.partner`
- `ResUsers`
- `theme.ir.asset`
- `theme.ir.ui.view`
- `theme.ir.attachment`
- `theme.website.menu`
- `theme.website.page`
- `IrUiView`
- `WebsiteMenu`
- `WebsitePage`
- `website`
- `website.configurator.feature`
- `website.controller.page`
- `Website`
- `ir.model`
- `IrModelFields`
- `website.menu`
- `website.page`
- `website.route`
- `website.rewrite`
- `website.snippet.filter`
- `website.technical.page`
- `website.track`
- `website.visitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website - Models and Relations
class IrActionsServer
class IrAsset
class IrAttachment
class IrModelData
class "ir.module.module" as ir_module_module
class IrRule
class IrUiMenu
class "ir.ui.view" as ir_ui_view
class ResCompany
class ResLang
class "res.partner" as res_partner
class ResUsers
class "theme.ir.asset" as theme_ir_asset
class "theme.ir.ui.view" as theme_ir_ui_view
class "theme.ir.attachment" as theme_ir_attachment
class "theme.website.menu" as theme_website_menu
class "theme.website.page" as theme_website_page
class IrUiView
class WebsiteMenu
class WebsitePage
class website
class "website.configurator.feature" as website_configurator_feature
class "website.controller.page" as website_controller_page
class Website
class "ir.model" as ir_model
class IrModelFields
class "website.menu" as website_menu
class "website.page" as website_page
class "website.route" as website_route
class "website.rewrite" as website_rewrite
class "website.snippet.filter" as website_snippet_filter
class "website.technical.page" as website_technical_page
class "website.track" as website_track
class "website.visitor" as website_visitor
IrAsset --> website : many2one
IrAttachment --> website : many2one
class "ir.attachment" as ir_attachment
ir_module_module --|> ir_attachment : one2many
ir_ui_view --> website : many2one
ir_ui_view --|> website_page : one2many
ir_ui_view --|> website_controller_page : one2many
ir_ui_view --> website_page : many2one
ResCompany --> website : many2one
res_partner --|> website_visitor : one2many
ResUsers --> website : many2one
class "ir.asset" as ir_asset
theme_ir_asset --|> ir_asset : one2many
theme_ir_ui_view --|> ir_ui_view : one2many
theme_ir_attachment --|> ir_attachment : one2many
theme_website_menu --> theme_website_page : many2one
theme_website_menu --> theme_website_menu : many2one
theme_website_menu --|> website_menu : one2many
theme_website_page --> theme_ir_ui_view : many2one
theme_website_page --|> website_page : one2many
IrUiView --> theme_ir_ui_view : many2one
WebsiteMenu --> theme_website_menu : many2one
WebsitePage --> theme_website_page : many2one
class "res.company" as res_company
website --> res_company : many2one
class "res.lang" as res_lang
website .. res_lang : many2many
website --> res_lang : many2one
class "res.users" as res_users
website --> res_users : many2one
website --> website_menu : many2one
website --> ir_module_module : many2one
website_configurator_feature --> ir_ui_view : many2one
website_configurator_feature --> ir_module_module : many2one
website_controller_page --> ir_ui_view : many2one
website_controller_page --> ir_ui_view : many2one
website_controller_page --|> website_menu : one2many
class "ir.model.fields" as ir_model_fields
ir_model --> ir_model_fields : many2one
website_menu --> website_page : many2one
website_menu --> website_controller_page : many2one
website_menu --> website : many2one
website_menu --> website_menu : many2one
website_menu --|> website_menu : one2many
class "res.groups" as res_groups
website_menu .. res_groups : many2many
website_page --> ir_ui_view : many2one
website_page --> res_users : many2one
website_page --|> website_menu : one2many
website_rewrite --> website : many2one
website_rewrite --> website_route : many2one
class "ir.actions.server" as ir_actions_server
website_snippet_filter --> ir_actions_server : many2one
class "ir.filters" as ir_filters
website_snippet_filter --> ir_filters : many2one
website_snippet_filter --> website : many2one
website_track --> website_visitor : many2one
website_track --> website_page : many2one
website_visitor --> website : many2one
website_visitor --> res_partner : many2one
class "res.country" as res_country
website_visitor --> res_country : many2one
website_visitor --> res_lang : many2one
website_visitor --|> website_track : one2many
website_visitor .. website_page : many2many
website_visitor --> website_page : many2one
@enduml
```

## Navigation

- [[../Community Addons/Community Addons|Back to category]]
- [[../../Odoo 19/Odoo 19|Back to version]]

<!-- GENERATED:MODULE -->
<!-- GENERATED:CATEGORY -->
---
tags: [odoo, v19, community, index, category]
---

# Website

Modules: 55

- [[Odoo 19/Community Addons/portal/portal|portal]]
- [[Odoo 19/Community Addons/website/website|website]]
- [[Odoo 19/Community Addons/website_blog/website_blog|website_blog]]
- [[Odoo 19/Community Addons/website_cf_turnstile/website_cf_turnstile|website_cf_turnstile]]
- [[Odoo 19/Community Addons/website_crm/website_crm|website_crm]]
- [[Odoo 19/Community Addons/website_crm_iap_reveal/website_crm_iap_reveal|website_crm_iap_reveal]]
- [[Odoo 19/Community Addons/website_crm_livechat/website_crm_livechat|website_crm_livechat]]
- [[Odoo 19/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- [[Odoo 19/Community Addons/website_crm_sms/website_crm_sms|website_crm_sms]]
- [[Odoo 19/Community Addons/website_customer/website_customer|website_customer]]
- [[Odoo 19/Community Addons/website_event/website_event|website_event]]
- [[Odoo 19/Community Addons/website_event_booth/website_event_booth|website_event_booth]]
- [[Odoo 19/Community Addons/website_event_booth_exhibitor/website_event_booth_exhibitor|website_event_booth_exhibitor]]
- [[Odoo 19/Community Addons/website_event_booth_sale/website_event_booth_sale|website_event_booth_sale]]
- [[Odoo 19/Community Addons/website_event_booth_sale_exhibitor/website_event_booth_sale_exhibitor|website_event_booth_sale_exhibitor]]
- [[Odoo 19/Community Addons/website_event_crm/website_event_crm|website_event_crm]]
- [[Odoo 19/Community Addons/website_event_exhibitor/website_event_exhibitor|website_event_exhibitor]]
- [[Odoo 19/Community Addons/website_event_sale/website_event_sale|website_event_sale]]
- [[Odoo 19/Community Addons/website_event_track/website_event_track|website_event_track]]
- [[Odoo 19/Community Addons/website_event_track_live/website_event_track_live|website_event_track_live]]
- [[Odoo 19/Community Addons/website_event_track_live_quiz/website_event_track_live_quiz|website_event_track_live_quiz]]
- [[Odoo 19/Community Addons/website_event_track_quiz/website_event_track_quiz|website_event_track_quiz]]
- [[Odoo 19/Community Addons/website_forum/website_forum|website_forum]]
- [[Odoo 19/Community Addons/website_google_map/website_google_map|website_google_map]]
- [[Odoo 19/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]]
- [[Odoo 19/Community Addons/website_hr_recruitment_livechat/website_hr_recruitment_livechat|website_hr_recruitment_livechat]]
- [[Odoo 19/Community Addons/website_links/website_links|website_links]]
- [[Odoo 19/Community Addons/website_livechat/website_livechat|website_livechat]]
- [[Odoo 19/Community Addons/website_mail/website_mail|website_mail]]
- [[Odoo 19/Community Addons/website_mail_group/website_mail_group|website_mail_group]]
- [[Odoo 19/Community Addons/website_mass_mailing/website_mass_mailing|website_mass_mailing]]
- [[Odoo 19/Community Addons/website_mass_mailing_sms/website_mass_mailing_sms|website_mass_mailing_sms]]
- [[Odoo 19/Community Addons/website_partner/website_partner|website_partner]]
- [[Odoo 19/Community Addons/website_payment/website_payment|website_payment]]
- [[Odoo 19/Community Addons/website_profile/website_profile|website_profile]]
- [[Odoo 19/Community Addons/website_project/website_project|website_project]]
- [[Odoo 19/Community Addons/website_sale/website_sale|website_sale]]
- [[Odoo 19/Community Addons/website_sale_autocomplete/website_sale_autocomplete|website_sale_autocomplete]]
- [[Odoo 19/Community Addons/website_sale_collect/website_sale_collect|website_sale_collect]]
- [[Odoo 19/Community Addons/website_sale_collect_wishlist/website_sale_collect_wishlist|website_sale_collect_wishlist]]
- [[Odoo 19/Community Addons/website_sale_comparison/website_sale_comparison|website_sale_comparison]]
- [[Odoo 19/Community Addons/website_sale_comparison_wishlist/website_sale_comparison_wishlist|website_sale_comparison_wishlist]]
- [[Odoo 19/Community Addons/website_sale_gelato/website_sale_gelato|website_sale_gelato]]
- [[Odoo 19/Community Addons/website_sale_loyalty/website_sale_loyalty|website_sale_loyalty]]
- [[Odoo 19/Community Addons/website_sale_mass_mailing/website_sale_mass_mailing|website_sale_mass_mailing]]
- [[Odoo 19/Community Addons/website_sale_mondialrelay/website_sale_mondialrelay|website_sale_mondialrelay]]
- [[Odoo 19/Community Addons/website_sale_slides/website_sale_slides|website_sale_slides]]
- [[Odoo 19/Community Addons/website_sale_stock/website_sale_stock|website_sale_stock]]
- [[Odoo 19/Community Addons/website_sale_stock_wishlist/website_sale_stock_wishlist|website_sale_stock_wishlist]]
- [[Odoo 19/Community Addons/website_sale_wishlist/website_sale_wishlist|website_sale_wishlist]]
- [[Odoo 19/Community Addons/website_slides/website_slides|website_slides]]
- [[Odoo 19/Community Addons/website_slides_forum/website_slides_forum|website_slides_forum]]
- [[Odoo 19/Community Addons/website_slides_survey/website_slides_survey|website_slides_survey]]
- [[Odoo 19/Community Addons/website_sms/website_sms|website_sms]]
- [[Odoo 19/Community Addons/website_timesheet/website_timesheet|website_timesheet]]
<!-- GENERATED:CATEGORY -->
