<template>
    <el-container class="container">
        <el-main class="main">
            <el-row ><el-input v-model="input" placeholder="请输入内容"></el-input></el-row>
            <el-row ><el-input v-model="input" placeholder="请输入内容"></el-input></el-row>
            <el-row><el-button type="primary">主要按钮</el-button></el-row>
        </el-main>
    </el-container>
</template>

<script>
export default {
  data() {
    return {
      input: ''
    }
  }
}

</script>

<style lang="scss" scoped>
$bg:rgba(240, 242, 245, 1);
.container{
    background-color: $bg;
    .main{
        border-width: 0px;
        position: absolute;
        left: 420px;
        top: 180px;
        width: 460px;
        height: 460px;
        display: flex;
        font-family: '微软雅黑';
        font-weight: 400;
        font-style: normal;
        text-align: left;
        line-height: 20px;
    }
}

</style>
