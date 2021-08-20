import Vue from 'vue'
import Vuex from 'vuex'
import api from './services/api'
import router from './router'

Vue.use(Vuex)

const store = new Vuex.Store({
    strict: process.env.NODE_ENV !== 'production',
    state: {

        userId: 0,
        username: '',
        isLoggedIn: false
    },

    getters: {
        userId: state => state.userId,
        username: state => state.username,
        isLoggedIn: state => state.isLoggedIn
    },

    mutations: {
        set(state, payload) {
            state.userId = payload.user.id
            state.username = payload.user.username
            state.isLoggedIn = true
        },
        clear(state) {
            state.userId = 0
            state.username = ''
            state.isLoggedIn = false
        }
    },

    actions: {
        login(context, payload) {
            return api.post('/auth/jwt/create/', {
                'email': payload.email,
                'password': payload.password
            })
            .then(response => {
                localStorage.setItem('access', response.data.access)
                return context.dispatch('reload')
                .then(user => user)
            })
            .catch(() => {
                router.push('/login')
                alert('You can not login')
            })
        },

        logout(context) {
            localStorage.removeItem('access')
            context.commit('clear')
        },

        reload(context) {
            return api.get('/auth/users/me/')
            .then(response => {
                const user = response.data
                context.commit('set', {user: user})
                return user
            }).
            catch(() => {
                localStorage.removeItem('access')
                router.replace('/login')
            })
        }
    }
})

export default store