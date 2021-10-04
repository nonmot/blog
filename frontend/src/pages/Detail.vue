<template>
    <v-container>
        <v-row class="my-5">
            <v-col
                xl=9
                lg=9
                md=9
                sm=12
                cols=12
            >

                <loading v-show="isLoading"/>

                <v-card
                    id="content"
                    v-if="!isLoading"
                >
                    <small id="updated_at" v-if="article.updated_at"><v-icon style="vertical-align: bottom;">mdi-update</v-icon>{{ getFormattedDate(article.updated_at) }}</small>
                    <small id="category" v-if="article.category">
                        <v-icon>mdi-tag</v-icon>
                        <span
                            v-for="category_id in article.category"
                            :key="category_id"
                            class="mr-2"
                        >
                            {{ getCategory(category_id).name }}
                        </span>
                    </small>
                    <span><v-chip v-if="!article.is_published" color="pink">非公開</v-chip></span>

                    <div class="d-flex justify-end">
                        <v-btn
                            v-if="isLoggedIn"
                            class="red mx-2"
                            @click.prevent="deleteArticle"
                        >
                            削除
                        </v-btn>
                        <router-link
                            v-if="isLoggedIn"
                            :to="{name: 'update', params: {id: article.id}}"
                            tag="div"
                        >
                            <v-btn
                                class="blue"
                            >編集</v-btn>
                        </router-link>
                    </div>
                    <v-card-title id="content_title" class="text-md-h3">
                        {{ article.title }}
                    </v-card-title>
                    <markdown-it-vue class="md-body" :content="article.content"></markdown-it-vue>
                </v-card>
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
import Introduction from '../components/Introduction'
import Loading from '../components/Loading'

import MarkdownItVue from 'markdown-it-vue'

export default {
    components: {
        MarkdownItVue,
        Loading,
        Introduction,
    },

    data() {
        return {
            isLoggedIn: false,
            article: {},
            updated_at: null,
            isLoading: true,
            category: [],
            user: {}
        }
    },

    methods: {
        getArticle() {
            api.get('/blog/' + this.$route.params.id + '/')
            .then(response => {
                this.article = response.data
                this.updated_at = new Date(this.article.updated_at)
                this.getUserInfo(this.article.user)
                document.title = this.article.title + " - Mot's Diary"
                this.isLoading = false
            })
        },

        deleteArticle() {
            if (window.confirm('本当に削除しますか？')) {
                api.delete('/blog/' + this.$route.params.id)
                .then(() => {
                    this.$router.replace('/')
                })
                .catch((err) => {
                    console.log(err)
                })
            }
        },
    },

    created () {
        this.isLoggedIn = this.$store.getters.isLoggedIn
        this.getArticle()
        this.getTags()
    }
}
</script>

<style lang="scss">
    #content {
        background-color: #fff;
        border-radius: 5px;
        padding: 30px;

        &_title {
            font-size: 40px;
            font-weight: normal;

            @media screen and (max-width: 600px) {
                font-size: 30px;
            }
        }

        #updated_at {
            margin-right: 20px;
        }

        .md-body {
            h1 {
                padding: 0.5em;/*文字周りの余白*/
                color: #010101;/*文字色*/
                background: #eaf3ff;/*背景色*/
                border-bottom: solid 3px #516ab6;/*下線*/

                @media screen and (max-width: 600px) {
                    font-size: 25px;
                }
            }
        }
    }

    .accent {
        background-color: #fff !important;
    }
</style>