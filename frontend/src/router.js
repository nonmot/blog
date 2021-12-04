import Vue from 'vue'
import VueRouter from 'vue-router'
import store from './store'

import TopPage from './pages/TopPage'
import Detail from './pages/Detail'
import ArticlePost from './pages/ArticlePost'
import ArticleUpdate from './pages/ArticleUpdate'
import LoginPage from './pages/LoginPage'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: TopPage,
            meta: {
                description: "物理学科に在籍する大学生の書くブログです。主に物理のことやプログラミングのことについて書いています。"
            }
        },
        {
            path: '/category/:category',
            component: TopPage
        },
        {
            path: '/article/post',
            component: ArticlePost,
            meta: {requireAuth: true}
        },
        {
            path: '/article/:id',
            component: Detail,
            name: 'detail'
        },{
            path: '/article/:id/update',
            component: ArticleUpdate,
            name: 'update',
            meta: {requireAuth: true}
        },
        {
            path: '/login',
            component: LoginPage
        }
    ]
})

router.beforeEach((to, from, next) => {
    if (to.meta.description) {
        document.querySelector("meta[name='description']").setAttribute('content', to.meta.description)
    }

    const isLoggedIn = store.getters.isLoggedIn
    const token = localStorage.getItem('access')

    if (token != null) {
        store.dispatch('reload')
    }

    // ログインが必要な画面に遷移しようとした場合
    if(to.matched.some(record => record.meta.requireAuth)) {
        // 既にログインしている場合
        if(isLoggedIn) {
            next()
        } else {
            // ログインしていない場合
            // まだ認証用トークンが残っていればユーザー情報を再取得
            if(token != null) {
                store.dispatch('reload')
                .then(() => {
                    // 再取得出来たらそのまま次へ
                    next()
                })
                .catch(() => {
                    store.dispatch('logout')
                    forceToLoginPage(to, from, next)
                })
            } else {
                // 認証用トークンがなければログイン画面へ
                forceToLoginPage(to, from, next)
            }
        }
    } else {
        next()
    }
})

function forceToLoginPage(to, from, next) {
    next({
        path: '/login',
        query: {next: to.fullPath}
    })
}

export default router