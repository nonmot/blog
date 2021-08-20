import api from '../services/api'

export default {
    methods: {
        // サーバーから全てのカテゴリーを取得する
        getTags() {
            api.get('category/')
            .then(response => {
                this.category = response.data
            })
        },

        // カテゴリーのIDを受け取ってカテゴリー名を返す
        getCategory(id) {
            return this.category.find(category => category.id === id)
        },

        // 日付を受け取って整形された日付を返す
        getFormattedDate(date) {
            const updated_at =  new Date(date)
            return updated_at.getFullYear() + '/' + (updated_at.getMonth() + 1) + '/' + updated_at.getDate()
        },

        // ユーザー情報の取得
        getUserInfo(id) {
            if (id) {
                api.get('user/' + id + '/')
                .then(response => {
                    this.user = response.data
                })
            } else {
                api.get('owner/')
                .then(response => {
                    this.user = response.data
                })
            }
        }
    }
}