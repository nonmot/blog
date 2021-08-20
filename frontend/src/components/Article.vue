<template>
    <div>
        <v-list>
            <template
                v-for="(article, index) in articles"
            >
                <v-list-item
                    :to="{name: 'detail', params: {id: article.id}}"
                    :key="article.title"
                >
                    <v-list-item-content>
                        <small><v-icon size=17 style="vertical-align: bottom;">mdi-update</v-icon>{{ getFormattedDate(article.updated_at) }}</small>
                        <span><v-chip v-if="!article.is_published" color="pink">非公開</v-chip></span>
                        <v-list-item-title>{{ article.title }}</v-list-item-title>
                        <small v-if="article.category">
                            <v-icon size=15>mdi-tag</v-icon>
                            <span
                                v-for="category_id in article.category"
                                :key="category_id"
                            >
                                {{ getCategory(category_id).name }}

                            </span>
                        </small>
                    </v-list-item-content>
                </v-list-item>
                <v-divider
                    v-if="index < articles.length - 1"
                    :key="index"
                ></v-divider>
            </template>
        </v-list>
    </div>
</template>

<script>
export default {
    props: ["articles", "category"],
}
</script>

<style scoped>
    .article_item {
        color: inherit;
        text-decoration: none;
    }
</style>