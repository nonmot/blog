<template>
    <v-footer
        dark
    >
        <v-col
            class="text-center"
            cols="12"
        >
            {{ new Date().getFullYear() }} - <strong>Mot's Diary</strong>
        </v-col>
    </v-footer>
</template>

<style scoped lang="scss">
    footer {
        margin-top: 50px;
    }
</style>