<template>
    <div>
        <v-app-bar
            app
            dark
            absolute
        >
            <div class="d-flex align-center">
                <router-link
                    to="/"
                    class="header_title"
                >
                    <h2>Mot's Diary</h2>
                </router-link>
            </div>

            <v-spacer></v-spacer>

            <v-menu
                offset-y
            >
                <template
                    v-slot:activator="{on, attrs}"
                >
                    <v-btn
                        v-bind="attrs"
                        v-on="on"
                    >
                        <v-icon>mdi-dots-horizontal</v-icon>
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item
                        v-if="getIsLoggedIn()"
                    >
                        <small>{{ getUsername() }}としてログインしています</small>
                    </v-list-item>

                    <v-list-item
                        v-if="!getIsLoggedIn()"
                    >
                        <router-link
                            to="/login"
                            tag="button"
                        >ログイン</router-link>
                    </v-list-item>

                    <v-list-item
                        v-if="getIsLoggedIn()"
                    >
                        <router-link
                            to="/article/post"
                            tag="button"
                        >投稿</router-link>
                    </v-list-item>
                    <v-list-item
                        v-if="getIsLoggedIn()"
                    >
                        <v-btn
                            @click="clickLogout"
                        >ログアウト</v-btn>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-app-bar>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            isLoggedIn: false
        }
    },

    methods: {
        clickLogout() {
            this.$store.dispatch('logout')
        },

        getIsLoggedIn() {
            this.isLoggedIn = this.$store.getters.isLoggedIn
            return this.isLoggedIn
        },

        getUsername() {
            if (this.isLoggedIn) {
                this.username = this.$store.getters.username
                return this.username
            }
        }
    },
}
</script>

<style scoped lang="scss">
    .header_title {
        text-decoration: none;
        color: inherit;
    }
</style>