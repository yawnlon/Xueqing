<template>
    <div class="footer-container" id="app-footer">
      <span style="font-family:'ArialMT', 'Arial';text-decoration:none;">Copyright © </span>
      <span style="font-family:'PingFangSC-Regular', 'PingFang SC';text-decoration:none;">好学知</span>
      <span style="font-family:'ArialMT', 'Arial';text-decoration:none;">, All Rights Reserved.</span>
    </div>
</template>
 
<script>
    export default {
        name: 'app-footer',
        data () {
            return {
            }
        }
    }
</script>
<style>
.footer-container {
    width: 100%;
    position: fixed;
    bottom: 20px;
    text-align: center;
    font-size: 12px;
    color: #FFFFFF;
    line-height: 24px;
  }
</style>