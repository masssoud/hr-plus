<template>
    <div>
        <Header></Header>
        <div class="uk-section uk-section-small uk-flex uk-flex-middle uk-text-center"
             style="min-height: calc((100vh - 80px));">
            <div class="uk-width-3-5 uk-margin-auto">
                <div class="uk-container">
                    <article class="uk-article">
                        <h1 class="uk-article-title">اچ‌آرپلاس!</h1>
                        <p class="uk-article-meta">ما با این سیستم سعی داریم تا به شما
                            نیروهای واحد منابع انسانی کمک کنیم تا به بهترین روش
                            کلیه فرآیندهای مرتبط خودتون را انجام بدید.</p>
                        <div class="uk-column-1-2@s uk-column-1-4@m  uk-text-center">
                            <div class="value-item">
                                <div class="value-icon bg-agility">
                                    <img src="../assets/images/Agility.svg" alt="Agility" uk-img>
                                </div>
                                <p class="uk-text-muted uk-text-small uk-margin-remove-bottom">Agility</p>
                                <p class="uk-text-bold uk-margin-remove-top">چابکی</p>
                            </div>
                            <div class="value-item">
                                <div class="value-icon bg-empowerment">
                                    <img src="../assets/images/Empowerment.svg" alt="Empowerment" uk-img>
                                </div>
                                <p class="uk-text-muted uk-text-small uk-margin-remove-bottom">Empowerment</p>
                                <p class="uk-text-bold uk-margin-remove-top">توانمندسازی</p>
                            </div>
                            <div class="value-item">
                                <div class="value-icon bg-responsibility">
                                    <img src="../assets/images/Responsibility.svg" alt="Responsibility" uk-img>
                                </div>
                                <p class="uk-text-muted uk-text-small uk-margin-remove-bottom">Responsibility</p>
                                <p class="uk-text-bold uk-margin-remove-top">مسئولیت‌پذیری</p>
                            </div>
                            <div class="value-item">
                                <div class="value-icon bg-respect">
                                    <img src="../assets/images/Respect.svg" alt="Respect" uk-img>
                                </div>
                                <p class="uk-text-muted uk-text-small uk-margin-remove-bottom">Respect</p>
                                <p class="uk-text-bold uk-margin-remove-top">احترام</p>
                            </div>
                        </div>
                        <p>نسخه 0.1</p>
                    </article>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from '../components/Header';

    export default {
        name: 'Home',
        components: {
            Header,
        },
        props: {
            msg: String
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
    .value-item {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 30px;
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    .value-icon {
        width: 80px;
        height: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        position: relative;

        img {
            position: relative;
            z-index: 10;
            width: 40px;
            height: auto;
        }
    }
</style>