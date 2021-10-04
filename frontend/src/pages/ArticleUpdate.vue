<template>
    <v-container>
        <ArticleForm :form="form" @submit="updateArticle" @selected="selected" :selectedCategory="selectedCategory"/>
    </v-container>
</template>

<script>
import api from '../services/api'
import ArticleForm from '../components/ArticleForm'

export default {
    components: {
        ArticleForm,
    },

    data() {
        return {
            form: {
                title: String,
                content: String,
            },
            selectedCategory: Array
        }
    },

    methods: {
        getArticle() {
            api.get('/blog/' + this.$route.params.id + '/')
            .then(response => {
                this.form.title = response.data.title
                this.form.content = response.data.content
                this.form.selectedCategory = response.data.category
            })
        },
        updateArticle() {
            api.put('/blog/' + this.$route.params.id + '/', {
                user: this.$store.getters.userId,
                title: this.form.title,
                content: this.form.content,
                category: this.form.selectedCategory
            })
            .then(() => {
                this.$router.replace('/article/' + this.$route.params.id)
            })
        },

        selected(category) {
            this.selectedCategory = category
        }
    },

    created() {
        this.getArticle()
    }
}
</script>