<template>
  <div class="success-container">
    <el-form  class="success-form" label-position="left">
      <img class="logo-img" src="https://d1icd6shlvmxi6.cloudfront.net/gsc/B9ZVTW/b0/9d/72/b09d72ea0aea4dfb8d84e2cd7dfc8743/images/登录界面/u17.png?token=4d192c476443f1295dab09fddbfdf13f043173a91298ee0f795dfcbea1871641"/>
      <img class="bingo" src=""/>
      <h3 class="tip1">{{tip}}</h3>
      <p class="tip2">请妥善保管您的账户信息</p>
      <el-button style="width:100%;margin-bottom:10px;margin-top:10px;background:#02a7f0" type="primary" @click.native.prevent="goHome">进入首页</el-button>
    </el-form>
    <div class="footer-container">
      <span style="font-family:'ArialMT', 'Arial';text-decoration:none;">Copyright © </span>
      <span style="font-family:'PingFangSC-Regular', 'PingFang SC';text-decoration:none;">好学知</span>
      <span style="font-family:'ArialMT', 'Arial';text-decoration:none;">, All Rights Reserved.</span>
    </div>
  </div>
</template>
<script>

export default {
  name: 'Success',
  data() {
    return {
      tip: '恭喜您注册成功'
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
    goHome() {

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
.success-container {
    margin: 0px;
    background-color: rgba(240, 242, 245, 1);
    background-image: none;
    position: relative;
    left: 0px;
    width: 678px;
    margin-left: auto;
    margin-right: auto;
    text-align: left;
}
</style>

<style lang="scss" scoped>

.success-container {
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
  .success-form {
    position: relative;
    background:#ffffff;
    width: 520px;
    max-width: 100%;
    padding: 2% 3%;
    margin: 5% auto;
    overflow: hidden;
    border-radius: 10px;
    text-align: center;
  }
  .logo-img {
    width: 100%;
    height: auto;
  }
  .bingo {
    position: relative;
    margin: auto;
    width: 100px;
    height: 100px
  }
  .tip1 {
    font-size: 24px;
    color: #666666;
  }
  .tip2 {
    font-size: 14px;
    color: #999999;
  }
  .svg-container {
    padding: 6px 5px 6px 15px;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }
  .footer-container {
    width: 100%;
    position: fixed;
    bottom: 20px;
    text-align: center;
    font-size: 12px;
    color: #FFFFFF;
    line-height: 24px;
  }
}
</style>
