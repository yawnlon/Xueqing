<template>
  <div class="success-container" :style="{backgroundImage: 'url(' + bg_img + ')' }">
    <el-form class="success-form" label-position="left">
      <img class="logo-img" :src="logo_img">
      <img class="bingo" src="">
      <h3 class="tip1">{{ tip }}</h3>
      <p class="tip2">请妥善保管您的账户信息</p>
      <el-button style="width:100%;margin-bottom:10px;margin-top:10px;background:#02a7f0" type="primary" @click.native.prevent="goHome">进入首页</el-button>
    </el-form>
    <app-footer />
  </div>
</template>
<script>
import Footer from '@/views/common/footer'
export default {
  name: 'Success',
  components: {
    'app-footer': Footer
  },
  data() {
    return {
      tip: '',
      logo_img: require('@/assets/front/logo-part3.png'),
      bg_img: require('@/assets/front/bg-01.png')
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
    this.tip = this.$route.query.tip
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    goHome() {
      this.$router.push({ path: '/dashboard' })
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
  background-color: rgba(2, 167, 240, 1);
  background-position: left top;
  background-repeat: repeat;
  background-attachment: scroll;
  background-size: 1751px 1038px;
  background-origin: border-box;
  .success-form {
    position: relative;
    background:#ffffff;
    width: 350px;
    height: 420px;
    max-width: 100%;
    padding: 1% 26px;
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
    margin-bottom: 10px;
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
}
</style>
