import { login, logout, getInfo } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import router, { resetRouter } from '@/router'

const state = {
  token: getToken(),
  name: '',
  avatar: '',
  introduction: '',
  roles: []
}

const mutations = {
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_INTRODUCTION: (state, introduction) => {
    state.introduction = introduction
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_ROLES: (state, roles) => {
    state.roles = roles
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    const { username, password,code } = userInfo
    let params='';
    if(code){
      params = { mobile: username.trim(),code:code }
    }else{
      params = { mobile: username.trim(), password: password }
    }
    return new Promise((resolve, reject) => {
      login(params).then(response => {
        // login({ username: username.trim(), password: password }).then(response => {  //for testing
        const { data } = response
        // console.log('hi')
        // console.log(response)
        data.token='admin-token'

        commit('SET_TOKEN', data.token)
        setToken(data.token)

        //改写，如果有detail,说明是直接登录返回的信息，而不是第三方登录，不需要用token再去获取用户信息
        //roles: ['admin'],
        //introduction: 'I am a super administrator',
        //avatar: 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        //name: 'Super Admin'
        // data.avatar='https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'
        // data.introduction='I am a super administrator'
        // if(data.user.id){
        //   commit('SET_ROLES', [data.user.type])
        //   commit('SET_NAME', data.user.username)
        //   commit('SET_AVATAR', data.avatar)//菜单栏，导航栏管理
        //   commit('SET_INTRODUCTION', data.introduction)//介绍信息
        // }
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    
    return new Promise((resolve, reject) => {
      // if(state.roles.length>0){
      //   //已经登录，不再用token去获取用户信息，直接跳转
      //   resolve({roles:state.roles})
      // }

      getInfo(state.token).then(response => {
        const { data } = response
        // console.log(data)
        if (!data) {
          reject('Verification failed, please Login again.')
        }

        const { roles, name, avatar, introduction } = data

        // roles must be a non-empty array
        if (!roles || roles.length <= 0) {
          reject('getInfo: roles must be a non-null array!')
        }

        commit('SET_ROLES', roles)
        commit('SET_NAME', name)
        commit('SET_AVATAR', avatar)
        commit('SET_INTRODUCTION', introduction)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        commit('SET_TOKEN', '')
        commit('SET_ROLES', [])
        removeToken()
        resetRouter()
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      commit('SET_TOKEN', '')
      commit('SET_ROLES', [])
      removeToken()
      resolve()
    })
  },

  // dynamically modify permissions
  changeRoles({ commit, dispatch }, role) {
    return new Promise(async resolve => {
      const token = role + '-token'

      commit('SET_TOKEN', token)
      setToken(token)

      const { roles } = await dispatch('getInfo')

      resetRouter()

      // generate accessible routes map based on roles
      const accessRoutes = await dispatch('permission/generateRoutes', roles, { root: true })

      // dynamically add accessible routes
      router.addRoutes(accessRoutes)

      // reset visited views and cached views
      dispatch('tagsView/delAllViews', null, { root: true })

      resolve()
    })
  },

  registerSucc({ commit, dispatch }, data){
    return new Promise(async resolve => {
      let roles = data.type

      const token = roles + '-token'
      commit('SET_TOKEN', token)
      setToken(token)

      commit('SET_ROLES', roles)
      commit('SET_NAME', data.name)
      commit('SET_AVATAR', 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif')
      commit('SET_INTRODUCTION', 'I am super admin')

      // generate accessible routes map based on roles
      const accessRoutes = await dispatch('permission/generateRoutes')

      // dynamically add accessible routes
      router.addRoutes(accessRoutes)

      resolve()
    })
  }

}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
