<template>
  <div class="signup-container" :style="{backgroundImage: 'url(' + bg_img + ')' }">
    <el-form ref="signupForm" :model="signupForm" :rules="signupRules" class="signup-form" autocomplete="on" label-position="left">
      <img class="logo-img" :src="logo_img">
      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="username"
          v-model="signupForm.username"
          placeholder="请输入姓名"
          name="username"
          type="text"
          tabindex="1"
          autocomplete="off"
        />
      </el-form-item>
      <el-form-item prop="phonenumber">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="phonenumber"
          v-model="signupForm.phonenumber"
          placeholder="请输入手机号码"
          name="phonenumber"
          type="text"
          tabindex="2"
          autocomplete="off"
        />
      </el-form-item>
      <el-form-item prop="valicode">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="valicode"
          v-model="signupForm.valicode"
          placeholder="请输入短信验证码"
          name="valicode"
          type="text"
          tabindex="3"
          autocomplete="off"
        />
        <el-button type="text" class="show-pwd" style="font-size:0.8em;" :disabled="codeDisabled" @click.native.prevent="sendCode(signupForm.phonenumber)">
          {{ codeMsg }}
        </el-button>
      </el-form-item>
      <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
        <el-form-item prop="password">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="signupForm.password"
            :type="passwordType"
            placeholder="设置6至20位登录密码"
            name="password"
            tabindex="4"
            autocomplete="on"
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false"
            @keyup.enter.native="handleSignup"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span>
        </el-form-item>
      </el-tooltip>
      <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
        <el-form-item prop="cpassword">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="cpassword"
            v-model="signupForm.cpassword"
            :type="passwordType"
            placeholder="请再次输入登录密码"
            name="cpassword"
            tabindex="5"
            autocomplete="on"
            @keyup.native="checkCapslock"
            @blur="capsTooltip = false"
            @keyup.enter.native="handleSignup"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span>
        </el-form-item>
      </el-tooltip>
      <el-checkbox v-model="signupForm.checked" style="color:#999999">勾选同意
        <router-link to="/agree" target="_blank">
          <span style="color:#666666">《用户服务协议》</span>
        </router-link>
      </el-checkbox>
      <el-button :loading="loading" type="primary" class="btn" @click.native.prevent="handleSignup('signupForm')">注册</el-button>
      <div class="login-container">
        <p><router-link to="/login"><span>已有账号，立即登录</span></router-link></p>
      </div>
    </el-form>
    <app-footer />
  </div>
</template>
<script>
import axios from 'axios'
import { MessageBox, Message } from 'element-ui'
import Footer from '@/views/common/footer'
export default {
  name: 'Signup',
  components: {
    'app-footer': Footer
  },
  data() {
    var validatePassword = (rule, value, callback) => {
      value = value + ''
      if (value === '') {
        callback(new Error('请输入密码'))
      } else if (value.length < 6 || value.length > 20) {
        callback(new Error('密码为6-20位字符'))
      } else {
        if (this.signupForm.cpassword !== '') {
          this.$refs.signupForm.validateField('cpassword')
        }
        callback()
      }
    }
    var validateCPassword = (rule, value, callback) => {
      value = value + ''
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.signupForm.password) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      signupForm: {
        checked: false
      },
      signupRules: {
        phonenumber: [
          { required: true, trigger: 'blur', message: '请输入手机号码' },
          { pattern: /^((1[3,5,8][0-9])|(14[5,7])|(17[0,5,6,7,8])|(19[7]))\d{8}$/, message: '请检查手机号是否正确', trigger: 'blur' }
        ],
        username: [
          { required: true, trigger: 'blur', message: '请输入姓名' }
        ],
        password: [
          { required: true, trigger: 'blur', validator: validatePassword }
        ],
        cpassword: [
          { required: true, trigger: 'blur', validator: validateCPassword }
        ],
        valicode: [
          { required: true, trigger: 'blur', message: '请输入短信验证码' },
          { len: 6, message: '短信验证码为6位数字', trigger: 'blur' }
        ]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {},
      logo_img: require('@/assets/front/logo-part3.png'),
      bg_img: require('@/assets/front/bg-01.png'),
      // 是否禁用按钮
      codeDisabled: false,
      // 倒计时秒数
      countdown: 60,
      // 按钮上的文字
      codeMsg: '发送验证码',
      // 定时器
      timer: null
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
    sendCode(phoneNum) {
      this.$refs.signupForm.validateField('phonenumber', (phoneError) => {
        console.log(`${phoneError}***************************`)
        if (!phoneError) {
          // 验证码60秒倒计时
          if (!this.timer) {
            axios
              .post('/api/v1/sms/send', { 'mobile': this.signupForm.phonenumber, 'check_mobile_exist': false, 'template': 'SMS_167655084' })
              .then(
                (response) => {
                  console.log(response)
                  this.codeDisabled = true
                  this.timer = setInterval(() => {
                    if (this.countdown > 0 && this.countdown <= 60) {
                      this.countdown--
                      if (this.countdown !== 0) {
                        this.codeMsg = '重新发送(' + this.countdown + ')'
                      } else {
                        clearInterval(this.timer)
                        this.codeMsg = '重发验证码'
                        this.countdown = 60
                        this.timer = null
                        this.codeDisabled = false
                      }
                    }
                  }, 1000)
                })
              .catch(function(error) { // 请求失败处理
                Message({
                  message: error.response.data.detail,
                  type: 'error',
                  duration: 5 * 1000
                })
                // console.log(error.response.data.detail)
              })
          }
        }
      })
    },
    handleSignup(formName) {
      this.$refs[formName].validate((valid) => {
        if (!this.signupForm.checked) {
          Message({
            message: '注册请同意《用户服务协议》',
            type: 'error',
            duration: 5 * 1000
          })
          return false
        }
        if (valid) {
          // this.loading = true
          axios
            .post('/api/v1/account/register', { 'name': this.signupForm.username, 'mobile': this.signupForm.phonenumber, 'code': this.signupForm.valicode, 'password': this.signupForm.password })
            .then(
              (response) => {
                console.log(response)
                this.loading = false
                this.$router.push({ path: '/success', query: { tip: '恭喜您注册成功' }})
              })
            .catch(function(error) { // 请求失败处理
              Message({
                message: error.response.data.detail,
                type: 'error',
                duration: 5 * 1000
              })
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
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

/* reset element-ui css */
.signup-container {
    margin: 0px;
    background-color: rgba(240, 242, 245, 1);
    background-image: none;
    position: relative;
    left: 0px;
    width: 678px;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
  .el-input {
      display: inline-block;
      height: 42px;
      width: 85%;
      input {
      font-weight: 400;
      font-style: normal;
      font-size: 14px;
      letter-spacing: normal;
      text-align: left;
      text-transform: none;
      border-color: transparent;
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 3px 2px;
      height: 42px;
    }
  }

  .el-form-item {
    border: 1px solid #d3d3d3;
    height:42px;
    width:298px;
    border-radius: 5px;
    // color: #454545;
    margin: 20px auto;
  }
}
</style>

<style lang="scss" scoped>

.signup-container {
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  background-color: rgba(2, 167, 240, 1);
  background-position: left top;
  background-repeat: repeat;
  background-attachment: scroll;
  background-size: 1751px 1038px;
  background-origin: border-box;
  .signup-form {
    position: relative;
    background:#ffffff;
    width: 350px;
    height: 589px;
    max-width: 100%;
    padding: 1% 26px;
    margin: 5% auto;
    overflow: hidden;
    border-radius: 10px;
    .login-container {
      margin: auto;
      text-align: center;
      font-weight: 400;
      font-style: normal;
      color: #02a7f0;
      p {
        text-decoration: none;
        font-size: 14px;
        position: relative;
        margin:  auto;
      }
    }
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
  .logo-img {
    width: 100%;
    height: auto;
    margin: 0;
  }
  .btn {
    width:100%;
    margin-bottom:10px;
    margin-top:10px;
    background: inherit;
    background-color: rgba(2, 167, 240, 1);
  }
  .btn:hover {
    background-color: rgba(2, 167, 240, 0.8);
  }
  .svg-container {
    padding: 0px 7px;
    vertical-align: middle;
    color: #889aa4;
    width: 30px;
    height: 42px;
    display: inline-block;
  }
  .show-pwd {
    position: absolute;
    right: 10px;
    top: 3px;
    font-size: 16px;
    cursor: pointer;
    user-select: none;
    color: #889aa4;
  }
}
</style>
