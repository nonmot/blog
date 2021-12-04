<template>
    <v-container>
        <Tags
            :tags="category"
        />
        <v-row>
            <v-col
                xl=9
                lg=9
                md=9
                sm=12
                cols=12
                class="d-flex flex-wrap"
            >
                <loading v-show="isLoading"/>

                <Article
                    :articles=blogs
                    :category=category
                    class="article"
                    v-show="!isLoading"
                ></Article>
            </v-col>
            <v-col
                xl=3
                lg=3
                md=3
                sm=12
                cols=12
            >
                <Introduction :user="user"/>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import api from '../services/api'

import Loading from '../components/Loading'
import Article from '../components/Article'
import Introduction from '../components/Introduction'
import Tags from '../components/Tags'

export default {
    components: {
        Article,
        Introduction,
        Loading,
        Tags,
    },

    data() {
        return {
            blogs: [],
            isLoading: true,
            category: [],
            user: {},
        }
    },

    methods: {
        getArticles() {
            api.get('blog/')
            .then(response => {
                this.blogs = response.data
                // 本当はここに書くのはよくないと思う
                // 非同期処理を学んだあとにもう一度書き直したい
                this.getUserInfo()
                this.isLoading = false
            })
        },

        getCategorizedArticle(category) {
            this.isLoading = true
            this.blogs = []
            api.get('blog/category/' + category + '/')
            .then(response => {
                this.blogs = response.data
                this.getUserInfo()
                this.isLoading = false
            })
        }
    },

    created() {
        this.getTags()
        this.getArticles()
        console.log("hello")

    },

    mounted() {
        document.title = "Mot's Diary"
    },

    watch: {
        '$route'(newCategory) {
            this.isLoading = true
            if (newCategory.params.category) {
                this.getCategorizedArticle(newCategory.params.category)
            } else {
                this.getArticles()
            }
            this.isLoading = false
        }
    }
}
</script>

<style scoped lang="scss">
    .article {
        width: 100%;
        background-color: #fff;
        padding: 20px;
    }
</style>
