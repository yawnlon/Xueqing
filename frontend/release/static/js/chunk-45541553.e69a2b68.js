(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-45541553"],{"0280":function(e,t,s){"use strict";s.r(t);var o=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("el-footer",{staticClass:"footer-container",attrs:{id:"app-footer"}},[s("span",{staticStyle:{"font-family":"'ArialMT', 'Arial'","text-decoration":"none"}},[e._v("Copyright © ")]),e._v(" "),s("span",{staticStyle:{"font-family":"'PingFangSC-Regular', 'PingFang SC'","text-decoration":"none"}},[e._v("好学知")]),e._v(" "),s("span",{staticStyle:{"font-family":"'ArialMT', 'Arial'","text-decoration":"none"}},[e._v(", All Rights Reserved.")])])},n=[],r={name:"AppFooter",data:function(){return{}}},a=r,i=(s("9af8"),s("2877")),c=Object(i["a"])(a,o,n,!1,null,null,null);t["default"]=c.exports},2359:function(e,t,s){"use strict";var o=s("5940"),n=s.n(o);n.a},"2e20":function(e,t,s){e.exports=s.p+"static/img/logo-part3.78f834eb.png"},5940:function(e,t,s){},8686:function(e,t,s){e.exports=s.p+"static/img/bg-01.38a48e01.png"},"87de":function(e,t,s){"use strict";s.r(t);var o=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"signup-container",style:{backgroundImage:"url("+e.bg_img+")"}},[s("el-form",{ref:"signupForm",staticClass:"signup-form",attrs:{model:e.signupForm,rules:e.signupRules,autocomplete:"on","label-position":"left"}},[s("img",{staticClass:"logo-img",attrs:{src:e.logo_img}}),e._v(" "),s("el-form-item",{attrs:{prop:"username"}},[s("span",{staticClass:"svg-container"},[s("svg-icon",{attrs:{"icon-class":"user"}})],1),e._v(" "),s("el-input",{ref:"username",attrs:{placeholder:"请输入姓名",type:"text",tabindex:"1",autocomplete:"off"},model:{value:e.signupForm.username,callback:function(t){e.$set(e.signupForm,"username",t)},expression:"signupForm.username"}})],1),e._v(" "),s("el-form-item",{attrs:{prop:"phonenumber"}},[s("span",{staticClass:"svg-container"},[s("svg-icon",{attrs:{"icon-class":"user"}})],1),e._v(" "),s("el-input",{ref:"phonenumber",attrs:{placeholder:"请输入手机号码",type:"text",name:"username",tabindex:"2",autocomplete:"off"},model:{value:e.signupForm.phonenumber,callback:function(t){e.$set(e.signupForm,"phonenumber",t)},expression:"signupForm.phonenumber"}})],1),e._v(" "),s("el-form-item",{attrs:{prop:"valicode"}},[s("span",{staticClass:"svg-container"},[s("svg-icon",{attrs:{"icon-class":"user"}})],1),e._v(" "),s("el-input",{ref:"valicode",attrs:{placeholder:"请输入短信验证码",type:"text",tabindex:"3",autocomplete:"off"},model:{value:e.signupForm.valicode,callback:function(t){e.$set(e.signupForm,"valicode",t)},expression:"signupForm.valicode"}}),e._v(" "),s("el-button",{staticClass:"show-pwd",staticStyle:{"font-size":"0.8em",color:"#02A7F0"},attrs:{type:"text",disabled:e.codeDisabled},nativeOn:{click:function(t){return t.preventDefault(),e.sendCode(e.signupForm.phonenumber)}}},[e._v("\n        "+e._s(e.codeMsg)+"\n      ")])],1),e._v(" "),s("el-tooltip",{attrs:{content:"Caps lock is On",placement:"right",manual:""},model:{value:e.capsTooltip,callback:function(t){e.capsTooltip=t},expression:"capsTooltip"}},[s("el-form-item",{attrs:{prop:"password"}},[s("span",{staticClass:"svg-container"},[s("svg-icon",{attrs:{"icon-class":"password"}})],1),e._v(" "),s("el-input",{key:e.passwordType,ref:"password",attrs:{type:e.passwordType,placeholder:"设置6至20位登录密码",tabindex:"4",autocomplete:"on"},on:{blur:function(t){e.capsTooltip=!1}},nativeOn:{keyup:[function(t){return e.checkCapslock(t)},function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleSignup(t)}]},model:{value:e.signupForm.password,callback:function(t){e.$set(e.signupForm,"password",t)},expression:"signupForm.password"}}),e._v(" "),s("span",{staticClass:"show-pwd",on:{click:e.showPwd}},[s("svg-icon",{attrs:{"icon-class":"password"===e.passwordType?"eye":"eye-open"}})],1)],1)],1),e._v(" "),s("el-tooltip",{attrs:{content:"Caps lock is On",placement:"right",manual:""},model:{value:e.capsTooltip,callback:function(t){e.capsTooltip=t},expression:"capsTooltip"}},[s("el-form-item",{attrs:{prop:"cpassword"}},[s("span",{staticClass:"svg-container"},[s("svg-icon",{attrs:{"icon-class":"password"}})],1),e._v(" "),s("el-input",{key:e.passwordType,ref:"cpassword",attrs:{type:e.passwordType,placeholder:"请再次输入登录密码",tabindex:"5",autocomplete:"on"},on:{blur:function(t){e.capsTooltip=!1}},nativeOn:{keyup:[function(t){return e.checkCapslock(t)},function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.handleSignup(t)}]},model:{value:e.signupForm.cpassword,callback:function(t){e.$set(e.signupForm,"cpassword",t)},expression:"signupForm.cpassword"}}),e._v(" "),s("span",{staticClass:"show-pwd",on:{click:e.showPwd}},[s("svg-icon",{attrs:{"icon-class":"password"===e.passwordType?"eye":"eye-open"}})],1)],1)],1),e._v(" "),s("el-checkbox",{staticStyle:{color:"#999999"},model:{value:e.signupForm.checked,callback:function(t){e.$set(e.signupForm,"checked",t)},expression:"signupForm.checked"}},[e._v("勾选同意\n      "),s("router-link",{attrs:{to:"/agree",target:"_blank"}},[s("span",{staticStyle:{color:"#666666"}},[e._v("《用户服务协议》")])])],1),e._v(" "),s("el-button",{staticClass:"btn",attrs:{loading:e.loading,type:"primary"},nativeOn:{click:function(t){return t.preventDefault(),e.handleSignup("signupForm")}}},[e._v("注册")]),e._v(" "),s("div",{staticClass:"login-container"},[s("p",[s("router-link",{attrs:{to:"/login"}},[s("span",[e._v("已有账号，立即登录")])])],1)])],1),e._v(" "),s("app-footer")],1)},n=[],r=(s("ac6a"),s("456d"),s("bc3a")),a=s.n(r),i=s("5c96"),c=s("0280"),l={name:"Signup",components:{"app-footer":c["default"]},data:function(){var e=this,t=function(t,s,o){s+="",""===s?o(new Error("请输入密码")):s.length<6||s.length>20?o(new Error("密码为6-20位字符")):(""!==e.signupForm.cpassword&&e.$refs.signupForm.validateField("cpassword"),o())},o=function(t,s,o){s+="",""===s?o(new Error("请再次输入密码")):s!==e.signupForm.password?o(new Error("两次输入密码不一致!")):o()};return{signupForm:{checked:!1},signupRules:{phonenumber:[{required:!0,trigger:"blur",message:"请输入手机号码"},{pattern:/^((1[3,5,8][0-9])|(14[5,7])|(17[0,5,6,7,8])|(19[7]))\d{8}$/,message:"请检查手机号是否正确",trigger:"blur"}],username:[{required:!0,trigger:"blur",message:"请输入姓名"}],password:[{required:!0,trigger:"blur",validator:t}],cpassword:[{required:!0,trigger:"blur",validator:o}],valicode:[{required:!0,trigger:"blur",message:"请输入短信验证码"},{len:6,message:"短信验证码为6位数字",trigger:"blur"}]},passwordType:"password",capsTooltip:!1,loading:!1,showDialog:!1,redirect:void 0,otherQuery:{},logo_img:s("2e20"),bg_img:s("8686"),codeDisabled:!1,countdown:60,codeMsg:"发送验证码",timer:null,message:""}},watch:{$route:{handler:function(e){var t=e.query;t&&(this.redirect=t.redirect,this.otherQuery=this.getOtherQuery(t))},immediate:!0}},created:function(){},mounted:function(){},destroyed:function(){},methods:{checkCapslock:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=e.shiftKey,s=e.key;s&&1===s.length&&(this.capsTooltip=!!(t&&s>="a"&&s<="z"||!t&&s>="A"&&s<="Z")),"CapsLock"===s&&!0===this.capsTooltip&&(this.capsTooltip=!1)},showPwd:function(){var e=this;"password"===this.passwordType?this.passwordType="":this.passwordType="password",this.$nextTick(function(){e.$refs.password.focus()})},sendCode:function(e){var t=this;this.$refs.signupForm.validateField("phonenumber",function(e){if(console.log("".concat(e,"***************************")),!e){var s=t;t.timer||a.a.post("/api/v1/sms/send",{mobile:t.signupForm.phonenumber,check_mobile_exist:!1,template:"SMS_167655084"}).then(function(e){console.log(e),t.codeDisabled=!0,t.timer=setInterval(function(){t.countdown>0&&t.countdown<=60&&(t.countdown--,0!==t.countdown?t.codeMsg="重新发送("+t.countdown+")":(clearInterval(t.timer),t.codeMsg="重发验证码",t.countdown=60,t.timer=null,t.codeDisabled=!1))},1e3),s.message&&s.message.close(),s.message=Object(i["Message"])({message:"验证码发送成功",type:"sucess",duration:5e3})}).catch(function(e){Object(i["Message"])({message:e.response.data.detail,type:"error",duration:5e3})})}})},handleSignup:function(e){var t=this;this.$refs[e].validate(function(e){return t.signupForm.checked?e?void a.a.post("/api/v1/account/register",{name:t.signupForm.username,mobile:t.signupForm.phonenumber,code:t.signupForm.valicode,password:t.signupForm.password}).then(function(e){t.$store.dispatch("user/registerSucc",e.data),console.log(e),t.loading=!1,t.$router.push({path:"/success",query:{tip:"恭喜您注册成功",redirect:"/",content:"进入首页"}})}).catch(function(e){Object(i["Message"])({message:e.response.data.detail,type:"error",duration:5e3})}):(console.log("error submit!!"),!1):(Object(i["Message"])({message:"注册请同意《用户服务协议》",type:"error",duration:5e3}),!1)})},getOtherQuery:function(e){return Object.keys(e).reduce(function(t,s){return"redirect"!==s&&(t[s]=e[s]),t},{})}}},p=l,u=(s("2359"),s("abda"),s("2877")),d=Object(u["a"])(p,o,n,!1,null,"4733c3fe",null);t["default"]=d.exports},"9af8":function(e,t,s){"use strict";var o=s("e9b4"),n=s.n(o);n.a},abda:function(e,t,s){"use strict";var o=s("efdd"),n=s.n(o);n.a},e9b4:function(e,t,s){},efdd:function(e,t,s){}}]);