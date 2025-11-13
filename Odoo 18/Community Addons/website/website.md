<!-- GENERATED:MODULE -->
---
tags: [odoo, v18, community, module]
---

# Website

- Version: v18
- Category: community
- Source: odoo/addons/website
- Dependencies: [[Odoo 18/Community Addons/digest/digest|digest]], [[Odoo 18/Community Addons/web/web|web]], [[Odoo 18/Community Addons/web_editor/web_editor|web_editor]], [[Odoo 18/Community Addons/html_editor/html_editor|html_editor]], [[Odoo 18/Community Addons/http_routing/http_routing|http_routing]], [[Odoo 18/Community Addons/portal/portal|portal]], [[Odoo 18/Community Addons/social_media/social_media|social_media]], [[Odoo 18/Community Addons/auth_signup/auth_signup|auth_signup]], [[Odoo 18/Community Addons/mail/mail|mail]], [[Odoo 18/Community Addons/google_recaptcha/google_recaptcha|google_recaptcha]], [[Odoo 18/Community Addons/utm/utm|utm]]

## Summary

Enterprise website builder

## XML Artifacts (detected)

- Views: 54
- Actions: 23
- Menus: 23
- Rules (ir.rule): 8
- Access CSV entries: 43

## Detected Models

- `ir.actions.server`
- `IrAsset`
- `Attachment`
- `IrModelData`
- `IrRule`
- `IrUiMenu`
- `ir.ui.view`
- `Company`
- `Lang`
- `res.partner`
- `ResUsers`
- `theme.ir.asset`
- `theme.ir.ui.view`
- `theme.ir.attachment`
- `theme.website.menu`
- `theme.website.page`
- `IrUiView`
- `IrAttachment`
- `WebsiteMenu`
- `WebsitePage`
- `website`
- `website.configurator.feature`
- `website.controller.page`
- `website_form_config`
- `ir.model`
- `ir.model.fields`
- `website.menu`
- `website.page`
- `website.route`
- `website.rewrite`
- `website.snippet.filter`
- `website.track`
- `website.visitor`


```plantuml
@startuml
!include ../../../Templates/DiagramStyles.puml
title Website - Models and Relations
class "ir.actions.server" as ir_actions_server
class IrAsset
class Attachment
class IrModelData
class IrRule
class IrUiMenu
class "ir.ui.view" as ir_ui_view
class Company
class Lang
class "res.partner" as res_partner
class ResUsers
class "theme.ir.asset" as theme_ir_asset
class "theme.ir.ui.view" as theme_ir_ui_view
class "theme.ir.attachment" as theme_ir_attachment
class "theme.website.menu" as theme_website_menu
class "theme.website.page" as theme_website_page
class IrUiView
class IrAttachment
class WebsiteMenu
class WebsitePage
class website
class "website.configurator.feature" as website_configurator_feature
class "website.controller.page" as website_controller_page
class website_form_config
class "ir.model" as ir_model
class "ir.model.fields" as ir_model_fields
class "website.menu" as website_menu
class "website.page" as website_page
class "website.route" as website_route
class "website.rewrite" as website_rewrite
class "website.snippet.filter" as website_snippet_filter
class "website.track" as website_track
class "website.visitor" as website_visitor
IrAsset --> website : many2one
Attachment --> website : many2one
ir_ui_view --> website : many2one
ir_ui_view --|> website_page : one2many
ir_ui_view --|> website_controller_page : one2many
ir_ui_view --> website_page : many2one
Company --> website : many2one
res_partner --|> website_visitor : one2many
ResUsers --> website : many2one
class "ir.asset" as ir_asset
theme_ir_asset --|> ir_asset : one2many
theme_ir_ui_view --|> ir_ui_view : one2many
class "ir.attachment" as ir_attachment
theme_ir_attachment --|> ir_attachment : one2many
theme_website_menu --> theme_website_page : many2one
theme_website_menu --> theme_website_menu : many2one
theme_website_menu --|> website_menu : one2many
theme_website_page --> theme_ir_ui_view : many2one
theme_website_page --|> website_page : one2many
IrUiView --> theme_ir_ui_view : many2one
IrAttachment --> theme_ir_attachment : many2one
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
class "ir.module.module" as ir_module_module
website --> ir_module_module : many2one
website_configurator_feature --> ir_ui_view : many2one
website_configurator_feature --> ir_module_module : many2one
website_controller_page --> ir_ui_view : many2one
website_controller_page --> ir_ui_view : many2one
website_controller_page --|> website_menu : one2many
ir_model --> ir_model_fields : many2one
website_menu --> website_page : many2one
website_menu --> website_controller_page : many2one
website_menu --> website : many2one
website_menu --> website_menu : many2one
website_menu --|> website_menu : one2many
class "res.groups" as res_groups
website_menu .. res_groups : many2many
website_page --> ir_ui_view : many2one
website_page --|> website_menu : one2many
website_rewrite --> website : many2one
website_rewrite --> website_route : many2one
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
- [[../../Odoo 18/Odoo 18|Back to version]]

<!-- GENERATED:MODULE -->
<!-- GENERATED:CATEGORY -->
---
tags: [odoo, v18, community, index, category]
---

# Website

Modules: 58

- [[Odoo 18/Community Addons/portal/portal|portal]]
- [[Odoo 18/Community Addons/website/website|website]]
- [[Odoo 18/Community Addons/website_blog/website_blog|website_blog]]
- [[Odoo 18/Community Addons/website_cf_turnstile/website_cf_turnstile|website_cf_turnstile]]
- [[Odoo 18/Community Addons/website_crm/website_crm|website_crm]]
- [[Odoo 18/Community Addons/website_crm_iap_reveal/website_crm_iap_reveal|website_crm_iap_reveal]]
- [[Odoo 18/Community Addons/website_crm_livechat/website_crm_livechat|website_crm_livechat]]
- [[Odoo 18/Community Addons/website_crm_partner_assign/website_crm_partner_assign|website_crm_partner_assign]]
- [[Odoo 18/Community Addons/website_crm_sms/website_crm_sms|website_crm_sms]]
- [[Odoo 18/Community Addons/website_customer/website_customer|website_customer]]
- [[Odoo 18/Community Addons/website_event/website_event|website_event]]
- [[Odoo 18/Community Addons/website_event_booth/website_event_booth|website_event_booth]]
- [[Odoo 18/Community Addons/website_event_booth_exhibitor/website_event_booth_exhibitor|website_event_booth_exhibitor]]
- [[Odoo 18/Community Addons/website_event_booth_sale/website_event_booth_sale|website_event_booth_sale]]
- [[Odoo 18/Community Addons/website_event_booth_sale_exhibitor/website_event_booth_sale_exhibitor|website_event_booth_sale_exhibitor]]
- [[Odoo 18/Community Addons/website_event_crm/website_event_crm|website_event_crm]]
- [[Odoo 18/Community Addons/website_event_exhibitor/website_event_exhibitor|website_event_exhibitor]]
- [[Odoo 18/Community Addons/website_event_jitsi/website_event_jitsi|website_event_jitsi]]
- [[Odoo 18/Community Addons/website_event_meet/website_event_meet|website_event_meet]]
- [[Odoo 18/Community Addons/website_event_meet_quiz/website_event_meet_quiz|website_event_meet_quiz]]
- [[Odoo 18/Community Addons/website_event_sale/website_event_sale|website_event_sale]]
- [[Odoo 18/Community Addons/website_event_track/website_event_track|website_event_track]]
- [[Odoo 18/Community Addons/website_event_track_live/website_event_track_live|website_event_track_live]]
- [[Odoo 18/Community Addons/website_event_track_live_quiz/website_event_track_live_quiz|website_event_track_live_quiz]]
- [[Odoo 18/Community Addons/website_event_track_quiz/website_event_track_quiz|website_event_track_quiz]]
- [[Odoo 18/Community Addons/website_forum/website_forum|website_forum]]
- [[Odoo 18/Community Addons/website_google_map/website_google_map|website_google_map]]
- [[Odoo 18/Community Addons/website_hr_recruitment/website_hr_recruitment|website_hr_recruitment]]
- [[Odoo 18/Community Addons/website_jitsi/website_jitsi|website_jitsi]]
- [[Odoo 18/Community Addons/website_links/website_links|website_links]]
- [[Odoo 18/Community Addons/website_livechat/website_livechat|website_livechat]]
- [[Odoo 18/Community Addons/website_mail/website_mail|website_mail]]
- [[Odoo 18/Community Addons/website_mail_group/website_mail_group|website_mail_group]]
- [[Odoo 18/Community Addons/website_mass_mailing/website_mass_mailing|website_mass_mailing]]
- [[Odoo 18/Community Addons/website_mass_mailing_sms/website_mass_mailing_sms|website_mass_mailing_sms]]
- [[Odoo 18/Community Addons/website_membership/website_membership|website_membership]]
- [[Odoo 18/Community Addons/website_partner/website_partner|website_partner]]
- [[Odoo 18/Community Addons/website_payment/website_payment|website_payment]]
- [[Odoo 18/Community Addons/website_payment_authorize/website_payment_authorize|website_payment_authorize]]
- [[Odoo 18/Community Addons/website_profile/website_profile|website_profile]]
- [[Odoo 18/Community Addons/website_project/website_project|website_project]]
- [[Odoo 18/Community Addons/website_sale/website_sale|website_sale]]
- [[Odoo 18/Community Addons/website_sale_autocomplete/website_sale_autocomplete|website_sale_autocomplete]]
- [[Odoo 18/Community Addons/website_sale_collect/website_sale_collect|website_sale_collect]]
- [[Odoo 18/Community Addons/website_sale_comparison/website_sale_comparison|website_sale_comparison]]
- [[Odoo 18/Community Addons/website_sale_comparison_wishlist/website_sale_comparison_wishlist|website_sale_comparison_wishlist]]
- [[Odoo 18/Community Addons/website_sale_gelato/website_sale_gelato|website_sale_gelato]]
- [[Odoo 18/Community Addons/website_sale_loyalty/website_sale_loyalty|website_sale_loyalty]]
- [[Odoo 18/Community Addons/website_sale_mass_mailing/website_sale_mass_mailing|website_sale_mass_mailing]]
- [[Odoo 18/Community Addons/website_sale_mondialrelay/website_sale_mondialrelay|website_sale_mondialrelay]]
- [[Odoo 18/Community Addons/website_sale_slides/website_sale_slides|website_sale_slides]]
- [[Odoo 18/Community Addons/website_sale_stock/website_sale_stock|website_sale_stock]]
- [[Odoo 18/Community Addons/website_sale_stock_wishlist/website_sale_stock_wishlist|website_sale_stock_wishlist]]
- [[Odoo 18/Community Addons/website_sale_wishlist/website_sale_wishlist|website_sale_wishlist]]
- [[Odoo 18/Community Addons/website_slides/website_slides|website_slides]]
- [[Odoo 18/Community Addons/website_slides_forum/website_slides_forum|website_slides_forum]]
- [[Odoo 18/Community Addons/website_slides_survey/website_slides_survey|website_slides_survey]]
- [[Odoo 18/Community Addons/website_sms/website_sms|website_sms]]
<!-- GENERATED:CATEGORY -->
