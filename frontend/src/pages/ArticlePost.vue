<template>
    <v-container>
        <ArticleForm :form="form" @submit="postArticle()"/>
    </v-container>
</template>

<script>
import api from '../services/api'
import 'markdown-it-vue/dist/markdown-it-vue.css'

import ArticleForm from '../components/ArticleForm'

export default {
    components: {
        ArticleForm,
    },
    data() {
        return {
            form: {
                title: null,
                content: null,
            }
        }
    },

    methods: {
        postArticle() {
            api.post('/blog/', {
                user: this.$store.getters.userId,
                title: this.form.title,
                content: this.form.content
            })
            .then(response => {
                this.$router.replace('/')
                console.log(response.data)
            })
        }
    }
}
</script>