import moment from 'jalali-moment';

class JalaliDateHelper {
    static gregorianToJalali = (gregorian, jalaliFormat) => {
        const date = moment(gregorian);
        return date.locale('fa').format(jalaliFormat);
    };

    static humanReadable = (gregorian) => {
        const start = moment(new Date());
        const date = moment(gregorian);
        return date.locale('fa').from(start);
    };
}

export default JalaliDateHelper;