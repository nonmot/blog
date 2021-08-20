<template>
    <div id="profile">
        <h3 id="profile_header">プロフィール</h3>
        <div id="content">
            <v-img
                :src="user.image"
                id="profile_img"
                alt="プロフィール画像"
            ></v-img>
            <h3 id="profile_name">{{ user.username }}</h3>
            <p id="profile_introduction">{{ user.profile }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            user: Object
        },
    }
</script>

<style scoped lang="scss">

    #profile {
        background-color: #fff;
        border-radius: 5px;

        #profile_header {
            background: #272727;
            color: white;
            padding: 0.5em;
        }

        #content {
            padding: 0.5em;

            #profile_img {
                border-radius: 50%;
                height: 100px;
                width: 100px;
                margin: 0 auto;
            }

            #profile_name {
                text-align: center;
                margin-bottom: 20px;
            }

            #profile_introduction {
                font-size: 15px;
            }
            
        }
    }
</style>