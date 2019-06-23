<template>
  <el-footer id="app-footer" class="footer-container">
    <span style="font-family:'ArialMT', 'Arial';text-decoration:none;">Copyright © </span>
    <span style="font-family:'PingFangSC-Regular', 'PingFang SC';text-decoration:none;">好学知</span>
    <span style="font-family:'ArialMT', 'Arial';text-decoration:none;">, All Rights Reserved.</span>
  </el-footer>
</template>

<script>
export default {
  name: 'AppFooter',
  data() {
    return {
    }
  }
}
</script>
<style>
.footer-container {
    position: absolute;
    bottom: 5px;
    width: 100%;
    text-align: center;
    font-size: 12px;
    color: #FFFFFF;
    line-height: 24px;
    margin-top: -60px;
  }
</style>
