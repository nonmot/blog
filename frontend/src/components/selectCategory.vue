<template>
    <div>
        <select multiple v-model="selectedCategory">
            <option disabled>カテゴリーを選択</option>
            <option
                v-for="item in categories"
                :key="item.id"
                :value="item.id"
            >{{ item.name }}</option>
        </select>
        selectCategory:{{ selectedCategory }}
    </div>
</template>

<script>

export default {
    props: {
        categories: Array,
        selectedCategory: Array,
    },

    watch: {
        selectCategory() {
            this.$emit('selected', this.selectedCategory)
            console.log('changed')
        }
    }
}
</script>