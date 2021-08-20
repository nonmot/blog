<template>
    <v-form
        @submit.prevent="clickSubmit"
    >
        <v-text-field
                label="title"
                v-model="form.title"
            ></v-text-field>
            <v-row>
                <v-col
                    cpls="6"
                >
                    <v-textarea
                        label="content"
                        v-model="form.content"
                        rows=20
                    ></v-textarea>
                </v-col>
                <v-col
                    cols="6"
                >
                    <Markdown-it-vue class="md-body" :content="form.content"/>
                </v-col>
            </v-row>

            <select-category :categories="category" :selectedCategory="selectedCategory"/>
            
            <v-btn
                type="submit"
            >投稿</v-btn>

    </v-form>
</template>

<script>
import MarkdownItVue from 'markdown-it-vue'
import selectCategory from './selectCategory.vue'

export default {
    components: {
        MarkdownItVue,
        selectCategory,
    },

    props: {
        form: {
            title: String,
            content: String,
        },
        selectedCategory: Array,
    },

    data() {
        return {
            category: null,
        }
    },

    methods: {
        clickSubmit() {
            this.$emit('submit')
        }
    },

    created() {
        this.getTags()
    },
}
</script>

<style scoped lang="scss">
</style>