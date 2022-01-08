# WEB LINK CRAWLER

A simple tool to crawl all the backlinks in the website.

## Demo

```bash
#!/bin/bash
python3 .\webLinkCrawler.py

The links in the web page https://www.goodreads.com :
--------------------------------------------------------------

[+] https://www.goodreads.com/
[+] https://s.gr-assets.com/assets/facebook/goodreads_wide-e23f6858b6bf20dcaf8493237a214a0e.png
[+] http://schema.org/Organization
[+] https://goodreads.com/#organiation
[+] https://goodreads.com/
[+] https://www.twitter.com/goodreads/
[+] https://www.facebook.com/goodreads/
[+] https://www.instagram.com/goodreads/
[+] http://d.gr-assets.com/misc/1454549184-1454549184_goodreads_misc.jpg
[+] https://
[+] http://
[+] https://unagi.amazon.com/1/events/com.amazon.csm.csa.prod
[+] https://m.media-amazon.com/images/I/41mrkPcyPwL.js
[+] https://s.gr-assets.com/assets/webfontloader-a550a17efafeccd666200db5de8ec913.js
[+] https://s.gr-assets.com/assets/gr/fonts-e256f84093cc13b27f5b82343398031a.css
[+] https://s.gr-assets.com/assets/goodreads-f5a05574f552767736654703ec5bf063.css
[+] https://s.gr-assets.com/assets/gr/pages/home/signed_out_hp-67203c04fc851e906f5bc27874760001.css
[+] https://s.gr-assets.com/assets/common_images-670d97636259cafc355c94fc43e871d7.css
[+] https://s.gr-assets.com/assets/desktop/libraries-41a429a5834e6352d597e2cf0b06486f.js
[+] https://s.gr-assets.com/assets/application-7606609cafaf6fe4c5ef3af6b7d3302f.js
[+] https://s.gr-assets.com/assets/react_client_side/external_dependencies-2e2b90fafc.js
[+] https://s.gr-assets.com/assets/react_client_side/site_header-affe4ebd97.js
[+] https://s.gr-assets.com/assets/react_client_side/custom_react_ujs-b1220d5e0a4820e90b905c302fc5cb52.js
[+] https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js
[+] https://s.gr-assets.com/assets/home/header_logo-8d96d7078a3d63f9f31d92282fd67cf4.png
[+] https://www.facebook.com/v3.1/dialog/oauth?client_id=2415071772&amp;redirect_uri=https%3A%2F%2Fwww.goodreads.com%2Fuser%2Fnew&amp;scope=email%2Cuser_friends&amp;state=fb_oauth_state_f73df953-1178-46e3-8661-3e206987b2fa
[+] https://www.goodreads.com/amazon/login/redirect_to_amazon_login_url?inpopup=false
[+] https://www.goodreads.com/challenges/11636?ref=rc22_soh
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1433161048l/1137215._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1344409006l/142296._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1277163268l/7670800._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1284431932l/8253037._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320437674l/9222475._SY160_.jpg
[+] https://s.gr-assets.com/assets/home/discovery_arrow-f1e8677f2c8b68500ed82ef0d5b7c59b.png
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1348322381l/3450744._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320428955l/2776527._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1255573980l/1713426._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1479863624l/1618._SX98_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1317793965l/11468377._SX98_.jpg
[+] https://s.gr-assets.com/assets/home/discovery_arrow-f1e8677f2c8b68500ed82ef0d5b7c59b.png
[+] https://schema.org/WebSite
[+] https://goodreads.com/
[+] https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif
[+] https://s.gr-assets.com/assets/layout/magnifying_glass-a2d7514d50bcee1a0061f1ece7821750.png
[+] https://images.gr-assets.com/authors/1521044377p2/3565.jpg
[+] https://images.gr-assets.com/quotes/1511992603p8/8630.jpg
[+] https://images.gr-assets.com/quotes/1511992603p2/8630.jpg
[+] https://images.gr-assets.com/authors/1429114964p2/9810.jpg
[+] https://images.gr-assets.com/authors/1315160559p2/22302.jpg
[+] https://images.gr-assets.com/authors/1197881416p2/13755.jpg
[+] https://images.gr-assets.com/authors/1331977133p2/5768330.jpg
[+] https://images.gr-assets.com/authors/1282396130p2/1744830.jpg
[+] https://images.gr-assets.com/authors/1193930952p2/61105.jpg
[+] https://images.gr-assets.com/authors/1198551937p2/259666.jpg
[+] https://images.gr-assets.com/authors/1356810912p2/5810891.jpg
[+] https://images.gr-assets.com/authors/1605640483p2/7715.jpg
[+] https://images.gr-assets.com/authors/1596216614p2/1077326.jpg
[+] https://www.goodreads.com/book/show/6.Harry_Potter_and_the_Goblet_of_Fire?from_choice=false&amp;from_home_module=false\
[+] https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif\
[+] https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif\
[+] https://s.gr-assets.com/assets/loading-trans-ced157046184c3bc7c180ffbfc6825a4.gif\
[+] https://images.gr-assets.com/authors/1606568448p2/957894.jpg
[+] https://images.gr-assets.com/authors/1322103868p2/1244.jpg
[+] https://images.gr-assets.com/quotes/1387503187p8/10554.jpg
[+] https://images.gr-assets.com/quotes/1387503187p2/10554.jpg
[+] https://www.goodreads.com/book/show/30633.The_Four_Loves?from_choice=false&amp;from_home_module=false\
[+] https://images.gr-assets.com/authors/1379017377p2/3503.jpg
[+] https://images.gr-assets.com/authors/1216826209p2/114059.jpg
[+] https://images.gr-assets.com/authors/1521044377p2/3565.jpg
[+] https://images.gr-assets.com/authors/1521044377p2/3565.jpg
[+] https://images.gr-assets.com/authors/1356810912p2/5810891.jpg
[+] https://s.gr-assets.com/assets/award/2021/choice-logo-medium-dace949f52e2201655481056e1535a85.png
[+] https://www.goodreads.com/blog/show/2232-readers-most-anticipated-mysteries-of-2022?int=Soapbox_Signed_Out_2022_Jan&amp;int_sub=Blog_2232
[+] https://www.goodreads.com/blog/show/2232-readers-most-anticipated-mysteries-of-2022?int=Soapbox_Signed_Out_2022_Jan&amp;int_sub=Blog_2232
[+] https://images.gr-assets.com/blogs/1639434915p7/2232.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1553383690l/2657._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532714506l/40961427._SX50_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474154022l/3._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1490528560l/4671._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1622355533l/4667024._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1579036753l/77203._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1494428973l/43641._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1522157426l/19063._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1327868566l/2429135._SX50_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1638425885l/16299._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1639587647l/960._SY75_.jpg
[+] https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1386605169l/17899948._SX50_.jpg
[+] https://help.goodreads.com/s/article/Goodreads-Interest-Based-Ads-Notice
[+] https://www.facebook.com/Goodreads/
[+] https://s.gr-assets.com/assets/site_footer/footer_facebook-ea4ab848f8e86c5f5c98311bc9495a1b.svg
[+] https://twitter.com/goodreads
[+] https://s.gr-assets.com/assets/site_footer/footer_twitter-126b3ee80481a763f7fccb06ca03053c.svg
[+] https://www.instagram.com/goodreads/
[+] https://s.gr-assets.com/assets/site_footer/footer_instagram-d59e3887020f12bcdb12e6c539579d85.svg
[+] https://www.linkedin.com/company/goodreads-com/
[+] https://s.gr-assets.com/assets/site_footer/footer_linkedin-5b820f4703eff965672594ef4d10e33c.svg
[+] https://itunes.apple.com/app/apple-store/id355833469?pt=325668&amp;ct=mw_footer&amp;mt=8
[+] https://s.gr-assets.com/assets/app/badge-ios-desktop-homepage-6ac7ae16eabce57f6c855361656a7540.svg
[+] https://play.google.com/store/apps/details?id=com.goodreads&amp;utm_source=mw_footer&amp;pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1
[+] https://s.gr-assets.com/assets/app/badge-android-desktop-home-2x-e31514e1fb4dddecf9293aa526a64cfe.png 2x
[+] https://s.gr-assets.com/assets/app/badge-android-desktop-home-0f517cbae4d56c88a128d27a7bea1118.png
[+] https://s.gr-assets.com/assets/facebook/login_animation-085464711e6c1ed5ba287a2f40ba3343.gif
[+] https://secure
[+] http://pixel
[+] https://sb
[+] http://b
[+] https://sb.scorecardresearch.com/p?c1=2&amp;amp;c2=6035830&amp;amp;c3=&amp;amp;c4=&amp;amp;c5=&amp;amp;c6=&amp;amp;c15=&amp;amp;cv=2.0&amp;amp;cj=1
[+] https://www.goodreads.com/dfp/impression
[+] https://www.goodreads.com/dfp/click
[+] https://www.goodreads.com/dfp/impression
[+] https://www.goodreads.com/dfp/click
```
