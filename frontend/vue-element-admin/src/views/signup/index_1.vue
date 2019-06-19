<template>
  <div class="signup-container">
    <div class="title-container">
      <div class="mask"></div>
      <p><span>LOGO</span></p>
    </div>
    <el-form ref="signupForm" :model="signupForm" :rules="signupRules" class="signup-form" autocomplete="on" label-position="left">
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
          autocomplete="off"/>
        <span class="show-pwd" style="font-size:0.8em;color:#0079fe" @click="sendCode">
          发送验证码
        </span>
      </el-form-item>

      <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
        <el-form-item prop="password1">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password1"
            v-model="signupForm.password1"
            :type="passwordType"
            placeholder="设置6至20位登录密码"
            name="password1"
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
        <el-form-item prop="password2">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password2"
            v-model="signupForm.password2"
            :type="passwordType"
            placeholder="请再次输入登录密码"
            name="password2"
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
      <a href="" style="color:#666666">《用户服务协议》</a></el-checkbox>

      <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:10px;margin-top:10px;" @click.native.prevent="handleSignup">注册</el-button>

      <div  class="login-container">
          <p><router-link to="/login">
            <span>已有账号，立即登录</span>
          </router-link></p>
      </div>
    </el-form>
  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'

export default {
  name: 'Signup',
  // components: { SocialSign },
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      signupForm: {
        checked: false
      },
      signupRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {}
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
    if (this.signupForm.username === '') {
      this.$refs.username.focus()
    } else if (this.signupForm.phonenumber === '') {
      this.$refs.phonenumber.focus()
    } else if (this.signupForm.valicode === '') {
      this.$refs.valicode.focus()
    } else if (this.signupForm.password1 === '') {
      this.$refs.password1.focus()
    } else if (this.signupForm.password2 === '') {
      this.$refs.password2.focus()
    } else if (!this.signupForm.checked) {
      this.$refs.checked.focus()
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
    sendCode() {

    },
    handleSignup() {
      this.$refs.signupForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('user/signup', this.signupForm)
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
      height: 47px;
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
      padding: 12px 5px 12px 15px;
      height: 47px;
    }
  }

  .el-form-item {
    border: 1px solid rgba(240, 242, 245, 1);
    border-radius: 5px;
    // color: #454545;
  }
}
</style>

<style lang="scss" scoped>

.signup-container {
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  background-image: url(https://d1icd6shlvmxi6.cloudfront.net/gsc/B9ZVTW/b0/9d/72/b09d72ea0aea4dfb8d84e2cd7dfc8743/images/%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2/bg.png?token=06b4db5a27e8c8c7cdc1c704144ea1d83295329eb44f59066ba132011bcd237d);
  background-color: rgba(2, 167, 240, 1);
  background-position: left top;
  background-repeat: repeat;
  background-attachment: scroll;
  background-size: 1751px 1038px;
  background-origin: border-box;
  .signup-form {
    position: relative;
    background:#ffffff;
    width: 520px;
    max-width: 100%;
    padding: 5% 3%;
    margin: 0 auto;
    top: -70px;
    overflow: hidden;
    border-radius: 10px;
    .login-container {
      margin: auto;
      text-align: center;
      font-weight: 400;
      font-style: normal;
      color: #0079FE;
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

  .svg-container {
    padding: 6px 5px 6px 15px;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;
    margin: 5% auto 0;
    border-width: 0px;
    width: 140px;
    height: 140px;
    display: flex;
    font-weight: 700;
    font-style: normal;
    font-size: 20px;
    color: #999999;
    line-height: 36px;
    .mask {
      border-width: 0px;
      position: absolute;
      left: 0px;
      top: 0px;
      width: 140px;
      height: 140px;
      background: inherit;
      background-color: rgba(255, 255, 255, 1);
      border: none;
      border-radius: 284px;
      -moz-box-shadow: none;
      -webkit-box-shadow: none;
      box-shadow: none;
      font-weight: 700;
      font-style: normal;
      font-size: 20px;
      color: #999999;
      line-height: 36px;
    }
    p {
      position: relative;
      margin:  auto;
      z-index:100
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    cursor: pointer;
    user-select: none;
  }
}
</style>
