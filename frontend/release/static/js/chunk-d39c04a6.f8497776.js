(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-d39c04a6"],{"105d":function(e,t,n){"use strict";n.r(t);var o=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"icons-container"},[e._m(0),e._v(" "),n("el-tabs",{attrs:{type:"border-card"}},[n("el-tab-pane",{attrs:{label:"Icons"}},e._l(e.svgIcons,function(t){return n("div",{key:t,on:{click:function(n){e.handleClipboard(e.generateIconCode(t),n)}}},[n("el-tooltip",{attrs:{placement:"top"}},[n("div",{attrs:{slot:"content"},slot:"content"},[e._v("\n            "+e._s(e.generateIconCode(t))+"\n          ")]),e._v(" "),n("div",{staticClass:"icon-item"},[n("svg-icon",{attrs:{"icon-class":t,"class-name":"disabled"}}),e._v(" "),n("span",[e._v(e._s(t))])],1)])],1)}),0),e._v(" "),n("el-tab-pane",{attrs:{label:"Element-UI Icons"}},e._l(e.elementIcons,function(t){return n("div",{key:t,on:{click:function(n){e.handleClipboard(e.generateElementIconCode(t),n)}}},[n("el-tooltip",{attrs:{placement:"top"}},[n("div",{attrs:{slot:"content"},slot:"content"},[e._v("\n            "+e._s(e.generateElementIconCode(t))+"\n          ")]),e._v(" "),n("div",{staticClass:"icon-item"},[n("i",{class:"el-icon-"+t}),e._v(" "),n("span",[e._v(e._s(t))])])])],1)}),0)],1)],1)},c=[function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("aside",[n("a",{attrs:{href:"https://panjiachen.github.io/vue-element-admin-site/guide/advanced/icon.html",target:"_blank"}},[e._v("Add and use\n    ")])])}],a=n("f71e"),r=(n("3c6b"),n("f763"),n("51ff")),i=function(e){return e.keys()},s=/\.\/(.*)\.svg/,l=i(r).map(function(e){return e.match(s)[1]}),u=l,d=["info","error","success","warning","question","back","arrow-left","arrow-down","arrow-right","arrow-up","caret-left","caret-bottom","caret-top","caret-right","d-arrow-left","d-arrow-right","minus","plus","remove","circle-plus","remove-outline","circle-plus-outline","close","check","circle-close","circle-check","circle-close-outline","circle-check-outline","zoom-out","zoom-in","d-caret","sort","sort-down","sort-up","tickets","document","goods","sold-out","news","message","date","printer","time","bell","mobile-phone","service","view","menu","more","more-outline","star-on","star-off","location","location-outline","phone","phone-outline","picture","picture-outline","delete","search","edit","edit-outline","rank","refresh","share","setting","upload","upload2","download","loading"],p=d,f={name:"Icons",data:function(){return{svgIcons:u,elementIcons:p}},methods:{generateIconCode:function(e){return'<svg-icon icon-class="'.concat(e,'" />')},generateElementIconCode:function(e){return'<i class="el-icon-'.concat(e,'" />')},handleClipboard:function(e,t){Object(a["a"])(e,t)}}},m=f,v=(n("d305"),n("17cc")),h=Object(v["a"])(m,o,c,!1,null,"67c8faf8",null);t["default"]=h.exports},d305:function(e,t,n){"use strict";var o=n("d95f"),c=n.n(o);c.a},d95f:function(e,t,n){}}]);