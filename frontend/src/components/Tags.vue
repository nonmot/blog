<template>
    <v-card
        id="category"
    >
        <v-tabs
            dark
            show-arrows
        >
        <v-tabs-slider></v-tabs-slider>
            <v-tab
                to="/"
            >
                すべて
            </v-tab>
            <v-tab
                v-for="(tag, index) in tags"
                :key="index"
                :to="`/category/${tag.name}`"
            >
                {{ tag.name }}
            </v-tab>
        </v-tabs>
    </v-card>
</template>

<script>
export default {
    props: ["tags"],
}
</script>

<style scoped lang="scss">
    #category {
        margin-top: 30px;
        margin-bottom: 30px;
    }
</style>