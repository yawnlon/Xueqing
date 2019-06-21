<template>
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form u1_div ax_default" autocomplete="on" label-position="left">

      <!-- <div class="title-container">
        <h3 class="title">Login Form</h3>
      </div> -->
      <el-row>
      <div id="u18" class="ax_default image">
        <img id="u18_img" class="img" :src="log_img">
        <div id="u2_text" class="text ">
          <p><span style="text-decoration:none;" class="login_title">学清书院单词速记</span></p>
        </div>
      </div>
      </el-row>


      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          placeholder="Username"
          name="username"
          type="text"
          tabindex="1"
          autocomplete="on"
        />
      </el-form-item>

      <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
        <el-form-item prop="password">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="loginForm.password"
            :type="passwordType"
            placeholder="Password"
            name="password"
            tabindex="2"
            autocomplete="on"
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false"
            @keyup.enter.native="handleLogin"
          />
          
          <!-- <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span> -->
          <span class="show-pwd" style="font-size:0.8em" @click="sendCode">
            发送验证码
          </span>
        </el-form-item>
      </el-tooltip>
      <el-row class="login_font lgn_row_top">
        <el-col :span="12"><div class="grid-content bg-purple left">记住登录状态</div></el-col>
        <el-col :span="12"><div class="grid-content bg-purple-light right">忘记密码？</div></el-col>
      </el-row>
      <el-button :loading="loading" type="primary" class="u3_div" @click.native.prevent="handleLogin">登录</el-button>
      <el-row class="login_font lgn_row_bottom">
        <el-col :span="12"><div class="grid-content bg-purple left">手机验证码登录></div></el-col>
        <el-col :span="12"><div class="grid-content bg-purple-light right">注册新账号></div></el-col>
      </el-row>

      <!--<div style="position:relative">
        <div class="tips">
          <span>Username : admin</span>
          <span>Password : any</span>
        </div>
        <div class="tips">
          <span style="margin-right:18px;">Username : editor</span>
          <span>Password : any</span>
        </div>

         <el-button class="thirdparty-button" type="primary" @click="showDialog=true">
          Or connect with
        </el-button> 
      </div>-->
    </el-form>

    <el-dialog title="Or connect with" :visible.sync="showDialog">
      Can not be simulated on local, so please combine you own business simulation! ! !
      <br>
      <br>
      <br>
      <social-sign />
    </el-dialog>
  </div>
</template>

<script>
import log_img from '@/assets/front/u18.png'
import { validUsername } from '@/utils/validate'
import SocialSign from './components/SocialSignin'
import axios from 'axios'
import { MessageBox, Message } from 'element-ui'

export default {
  name: 'Login',
  // components: { SocialSign },
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    let m = null
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6&&value.length>0) {
        // callback(new Error('The password can not be less than 6 digits'))
        let error_msg = '密码不能低于6位'
        if(m){
          m.close()
          m = Message({
            message:error_msg,
            type:'error',
            duration: 5 * 1000
          })
        }else{
          m = Message({
            message:error_msg,
            type:'error',
            duration: 5 * 1000
          })
        }
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: 'admin',
        password: ''//'111111'
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {},
      log_img:log_img+ '?' + +new Date(),
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        const query = route.query
        if (query) {
          this.redirect = query.redirect
          this.otherQuery = this.getOtherQuery(query)
        }
      },
      immediate: true
    }
  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }

  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    checkCapslock({ shiftKey, key } = {}) {
      if (key && key.length === 1) {
        if (shiftKey && (key >= 'a' && key <= 'z') || !shiftKey && (key >= 'A' && key <= 'Z')) {
          this.capsTooltip = true
        } else {
          this.capsTooltip = false
        }
      }
      if (key === 'CapsLock' && this.capsTooltip === true) {
        this.capsTooltip = false
      }
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    sendCode(){
      axios
      .post('/api/sms/send',{'mobile':'18262610835','template':'SMS_167655084'})
      .then(response => (console.log(response)))
      .catch(function (error) { // 请求失败处理
            Message({
              message: error.response.data.detail,
              type: 'error',
              duration: 5 * 1000
            })
            // console.log(error.response.data.detail)
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
      // axios
      // .post('/api/account/login',{'mobile':'18262610835',})
      // .then(response => (console.log(response)))
      // .catch(function (error) { // 请求失败处理
      //     error => {
      //       Message({
      //         message: error.message,
      //         type: 'error',
      //         duration: 5 * 1000
      //       })
      //     }
      // })
      // return

        if (valid) {
          this.loading = true
          this.$store.dispatch('user/login', this.loginForm)
            .then(() => {
              this.$router.push({ path: this.redirect || '/', query: this.otherQuery })
              this.loading = false
            })
            .catch(() => {
              this.loading = false
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    }
    // afterQRScan() {
    //   if (e.key === 'x-admin-oauth-code') {
    //     const code = getQueryObject(e.newValue)
    //     const codeMap = {
    //       wechat: 'code',
    //       tencent: 'code'
    //     }
    //     const type = codeMap[this.auth_type]
    //     const codeName = code[type]
    //     if (codeName) {
    //       this.$store.dispatch('LoginByThirdparty', codeName).then(() => {
    //         this.$router.push({ path: this.redirect || '/' })
    //       })
    //     } else {
    //       alert('第三方登录失败')
    //     }
    //   }
    // }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray:#fff;
$cursor: #fff;
$more_gray:#999999;
$mycursor:#666;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;
    

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $more_gray;
      height: 47px;
      caret-color: $mycursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
    margin-left: 25px;
    margin-right:25px;
  }
}
</style>

<style lang="scss" scoped>
$bg:rgba(105, 43, 128, 1);
$dark_gray:#889aa4;
$light_gray:#eee;


.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;
  cursor:black;

  // .login-form {
  //   position: relative;
  //   width: 520px;
  //   max-width: 100%;
  //   padding: 160px 35px 0;
  //   margin: 0 auto;
  //   overflow: hidden;
  // }
  .left {
    text-align: left
  }
  .right{
    text-align: right
  }
  .u3_div {
    border-width: 0px;
    // position: absolute;
    left: 0px;
    top: 0px;
    width: 300px;
    height: 50px;
    background: inherit;
    background-color: rgba(105, 43, 128, 1);
    border: none;
    border-radius: 3px;
    -moz-box-shadow: none;
    -webkit-box-shadow: none;
    box-shadow: none;
    // font-family: '寰蒋闆呴粦 Regular', '寰蒋闆呴粦';
    font-weight: 400;
    font-style: normal;
    font-size: 18px;
    color: #FFFFFF;
}
  .u1_div {
    border-width: 0px;
    position: absolute;
    left: 0px;
    top: 0px;
    width: 350px;
    height: 420px;
    background: inherit;
    background-color: rgba(255, 255, 255, 1);
    border: none;
    border-radius: 10px;
    -moz-box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.349019607843137);
    -webkit-box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.349019607843137);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.349019607843137);
    // font-family: '寰蒋闆呴粦 Bold', '寰蒋闆呴粦 Regular', '寰蒋闆呴粦';
    font-weight: 700;
    font-style: normal;
    font-size: 16px;
    // color: #999999;
    color:black;
    text-align: left;
    line-height: 20px;
  }
  .login-form {
    position: fixed;
    left: 50%;
    margin-left: -175px;
    top: 50%;
    margin-top: -210px;
  }
  .ax_default {
    font-family: 'ArialMT', 'Arial';
    font-weight: 400;
    font-style: normal;
    font-size: 14px;
    letter-spacing: normal;
    color: #666666;
    vertical-align: none;
    text-align: center;
    line-height: normal;
    text-transform: none;
  }
  #u18_img {
    border-width: 0px;
    left: 0px;
    top: 0px;
    width: 249px;
    height: 98px;
    margin-top: 25px;
  }
  
  .login_title{
    font-family: 'PingFangSC-Regular', 'PingFang SC';
    font-weight: 400;
    font-style: normal;
    font-size: 24px;
    color: #692B80;
  }
  .lgn_row_top{
    height: 2.5em;
  }
  .lgn_row_bottom{
    margin-top:1em;
  }

  #u2_text{
    margin-top: -35px
  }

  .login_font{
    font-family: 'PingFangSC-Regular', 'PingFang SC';
    font-weight: 400;
    font-style: normal;
    font-size: 0.715em;
    color:#666666;
    margin-left:25px;
    margin-right:25px;
  }


  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }

  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: 6px;
  }

  @media only screen and (max-width: 470px) {
    .thirdparty-button {
      display: none;
    }
  }
}
</style>
