
/*
Auto-generated by CVXPYgen on January 30, 2024 at 06:19:45.
Content: Declarations for Python binding with pybind11.
*/

// User-defined parameters
struct CPG_Params_cpp_t {
    std::array<double, 3> q;
    std::array<double, 3> r_0;
    std::array<double, 3> v_0;
    double m_0;
    std::array<double, 36> t_f_A;
    std::array<double, 18> t_f_B;
    std::array<double, 18> t_f_B_g;
    double alpha;
    double theta_cos;
    std::array<double, 3> n_hat;
    double v_max;
    std::array<double, 3> c;
    std::array<double, 3> c_q;
    std::array<double, 120> rho_2_exp_z_0;
    std::array<double, 120> rho_2_exp_z_0_z_0;
    std::array<double, 120> rho_1_exp_z_0;
    std::array<double, 120> rho_1_exp_z_0_z_0;
};

// Flags for updated user-defined parameters
struct CPG_Updated_cpp_t {
    bool q;
    bool r_0;
    bool v_0;
    bool m_0;
    bool t_f_A;
    bool t_f_B;
    bool t_f_B_g;
    bool alpha;
    bool theta_cos;
    bool n_hat;
    bool v_max;
    bool c;
    bool c_q;
    bool rho_2_exp_z_0;
    bool rho_2_exp_z_0_z_0;
    bool rho_1_exp_z_0;
    bool rho_1_exp_z_0_z_0;
};

// Primal solution
struct CPG_Prim_cpp_t {
    std::array<double, 720> x;
    std::array<double, 120> sigma;
    std::array<double, 360> u;
    std::array<double, 120> z;
};

// Dual solution
struct CPG_Dual_cpp_t {
    std::array<double, 3> d0;
    std::array<double, 3> d1;
    double d2;
    std::array<double, 3> d3;
    double d4;
    std::array<double, 3> d5;
    std::array<double, 3> d6;
    std::array<double, 120> d7;
    std::array<double, 18> d8;
    double d9;
    std::array<double, 18> d10;
    double d11;
    std::array<double, 18> d12;
    double d13;
    std::array<double, 18> d14;
    double d15;
    std::array<double, 18> d16;
    double d17;
    std::array<double, 18> d18;
    double d19;
    std::array<double, 18> d20;
    double d21;
    std::array<double, 18> d22;
    double d23;
    std::array<double, 18> d24;
    double d25;
    std::array<double, 18> d26;
    double d27;
    std::array<double, 18> d28;
    double d29;
    std::array<double, 18> d30;
    double d31;
    std::array<double, 18> d32;
    double d33;
    std::array<double, 18> d34;
    double d35;
    std::array<double, 18> d36;
    double d37;
    std::array<double, 18> d38;
    double d39;
    std::array<double, 18> d40;
    double d41;
    std::array<double, 18> d42;
    double d43;
    std::array<double, 18> d44;
    double d45;
    std::array<double, 18> d46;
    double d47;
    std::array<double, 18> d48;
    double d49;
    std::array<double, 18> d50;
    double d51;
    std::array<double, 18> d52;
    double d53;
    std::array<double, 18> d54;
    double d55;
    std::array<double, 18> d56;
    double d57;
    std::array<double, 18> d58;
    double d59;
    std::array<double, 18> d60;
    double d61;
    std::array<double, 18> d62;
    double d63;
    std::array<double, 18> d64;
    double d65;
    std::array<double, 18> d66;
    double d67;
    std::array<double, 18> d68;
    double d69;
    std::array<double, 18> d70;
    double d71;
    std::array<double, 18> d72;
    double d73;
    std::array<double, 18> d74;
    double d75;
    std::array<double, 18> d76;
    double d77;
    std::array<double, 18> d78;
    double d79;
    std::array<double, 18> d80;
    double d81;
    std::array<double, 18> d82;
    double d83;
    std::array<double, 18> d84;
    double d85;
    std::array<double, 18> d86;
    double d87;
    std::array<double, 18> d88;
    double d89;
    std::array<double, 18> d90;
    double d91;
    std::array<double, 18> d92;
    double d93;
    std::array<double, 18> d94;
    double d95;
    std::array<double, 18> d96;
    double d97;
    std::array<double, 18> d98;
    double d99;
    std::array<double, 18> d100;
    double d101;
    std::array<double, 18> d102;
    double d103;
    std::array<double, 18> d104;
    double d105;
    std::array<double, 18> d106;
    double d107;
    std::array<double, 18> d108;
    double d109;
    std::array<double, 18> d110;
    double d111;
    std::array<double, 18> d112;
    double d113;
    std::array<double, 18> d114;
    double d115;
    std::array<double, 18> d116;
    double d117;
    std::array<double, 18> d118;
    double d119;
    std::array<double, 18> d120;
    double d121;
    std::array<double, 18> d122;
    double d123;
    std::array<double, 18> d124;
    double d125;
    std::array<double, 18> d126;
    double d127;
    std::array<double, 18> d128;
    double d129;
    std::array<double, 18> d130;
    double d131;
    std::array<double, 18> d132;
    double d133;
    std::array<double, 18> d134;
    double d135;
    std::array<double, 18> d136;
    double d137;
    std::array<double, 18> d138;
    double d139;
    std::array<double, 18> d140;
    double d141;
    std::array<double, 18> d142;
    double d143;
    std::array<double, 18> d144;
    double d145;
    std::array<double, 18> d146;
    double d147;
    std::array<double, 18> d148;
    double d149;
    std::array<double, 18> d150;
    double d151;
    std::array<double, 18> d152;
    double d153;
    std::array<double, 18> d154;
    double d155;
    std::array<double, 18> d156;
    double d157;
    std::array<double, 18> d158;
    double d159;
    std::array<double, 18> d160;
    double d161;
    std::array<double, 18> d162;
    double d163;
    std::array<double, 18> d164;
    double d165;
    std::array<double, 18> d166;
    double d167;
    std::array<double, 18> d168;
    double d169;
    std::array<double, 18> d170;
    double d171;
    std::array<double, 18> d172;
    double d173;
    std::array<double, 18> d174;
    double d175;
    std::array<double, 18> d176;
    double d177;
    std::array<double, 18> d178;
    double d179;
    std::array<double, 18> d180;
    double d181;
    std::array<double, 18> d182;
    double d183;
    std::array<double, 18> d184;
    double d185;
    std::array<double, 18> d186;
    double d187;
    std::array<double, 18> d188;
    double d189;
    std::array<double, 18> d190;
    double d191;
    std::array<double, 18> d192;
    double d193;
    std::array<double, 18> d194;
    double d195;
    std::array<double, 18> d196;
    double d197;
    std::array<double, 18> d198;
    double d199;
    std::array<double, 18> d200;
    double d201;
    std::array<double, 18> d202;
    double d203;
    std::array<double, 18> d204;
    double d205;
    std::array<double, 18> d206;
    double d207;
    std::array<double, 18> d208;
    double d209;
    std::array<double, 18> d210;
    double d211;
    std::array<double, 18> d212;
    double d213;
    std::array<double, 18> d214;
    double d215;
    std::array<double, 18> d216;
    double d217;
    std::array<double, 18> d218;
    double d219;
    std::array<double, 18> d220;
    double d221;
    std::array<double, 18> d222;
    double d223;
    std::array<double, 18> d224;
    double d225;
    std::array<double, 18> d226;
    double d227;
    std::array<double, 18> d228;
    double d229;
    std::array<double, 18> d230;
    double d231;
    std::array<double, 18> d232;
    double d233;
    std::array<double, 18> d234;
    double d235;
    std::array<double, 18> d236;
    double d237;
    std::array<double, 18> d238;
    double d239;
    std::array<double, 18> d240;
    double d241;
    std::array<double, 18> d242;
    double d243;
    std::array<double, 18> d244;
    double d245;
    double d246;
    double d247;
    double d248;
    std::array<double, 3> d249;
    double d250;
    double d251;
    double d252;
    double d253;
    double d254;
    std::array<double, 3> d255;
    double d256;
    double d257;
    double d258;
    double d259;
    double d260;
    std::array<double, 3> d261;
    double d262;
    double d263;
    double d264;
    double d265;
    double d266;
    std::array<double, 3> d267;
    double d268;
    double d269;
    double d270;
    double d271;
    double d272;
    std::array<double, 3> d273;
    double d274;
    double d275;
    double d276;
    double d277;
    double d278;
    std::array<double, 3> d279;
    double d280;
    double d281;
    double d282;
    double d283;
    double d284;
    std::array<double, 3> d285;
    double d286;
    double d287;
    double d288;
    double d289;
    double d290;
    std::array<double, 3> d291;
    double d292;
    double d293;
    double d294;
    double d295;
    double d296;
    std::array<double, 3> d297;
    double d298;
    double d299;
    double d300;
    double d301;
    double d302;
    std::array<double, 3> d303;
    double d304;
    double d305;
    double d306;
    double d307;
    double d308;
    std::array<double, 3> d309;
    double d310;
    double d311;
    double d312;
    double d313;
    double d314;
    std::array<double, 3> d315;
    double d316;
    double d317;
    double d318;
    double d319;
    double d320;
    std::array<double, 3> d321;
    double d322;
    double d323;
    double d324;
    double d325;
    double d326;
    std::array<double, 3> d327;
    double d328;
    double d329;
    double d330;
    double d331;
    double d332;
    std::array<double, 3> d333;
    double d334;
    double d335;
    double d336;
    double d337;
    double d338;
    std::array<double, 3> d339;
    double d340;
    double d341;
    double d342;
    double d343;
    double d344;
    std::array<double, 3> d345;
    double d346;
    double d347;
    double d348;
    double d349;
    double d350;
    std::array<double, 3> d351;
    double d352;
    double d353;
    double d354;
    double d355;
    double d356;
    std::array<double, 3> d357;
    double d358;
    double d359;
    double d360;
    double d361;
    double d362;
    std::array<double, 3> d363;
    double d364;
    double d365;
    double d366;
    double d367;
    double d368;
    std::array<double, 3> d369;
    double d370;
    double d371;
    double d372;
    double d373;
    double d374;
    std::array<double, 3> d375;
    double d376;
    double d377;
    double d378;
    double d379;
    double d380;
    std::array<double, 3> d381;
    double d382;
    double d383;
    double d384;
    double d385;
    double d386;
    std::array<double, 3> d387;
    double d388;
    double d389;
    double d390;
    double d391;
    double d392;
    std::array<double, 3> d393;
    double d394;
    double d395;
    double d396;
    double d397;
    double d398;
    std::array<double, 3> d399;
    double d400;
    double d401;
    double d402;
    double d403;
    double d404;
    std::array<double, 3> d405;
    double d406;
    double d407;
    double d408;
    double d409;
    double d410;
    std::array<double, 3> d411;
    double d412;
    double d413;
    double d414;
    double d415;
    double d416;
    std::array<double, 3> d417;
    double d418;
    double d419;
    double d420;
    double d421;
    double d422;
    std::array<double, 3> d423;
    double d424;
    double d425;
    double d426;
    double d427;
    double d428;
    std::array<double, 3> d429;
    double d430;
    double d431;
    double d432;
    double d433;
    double d434;
    std::array<double, 3> d435;
    double d436;
    double d437;
    double d438;
    double d439;
    double d440;
    std::array<double, 3> d441;
    double d442;
    double d443;
    double d444;
    double d445;
    double d446;
    std::array<double, 3> d447;
    double d448;
    double d449;
    double d450;
    double d451;
    double d452;
    std::array<double, 3> d453;
    double d454;
    double d455;
    double d456;
    double d457;
    double d458;
    std::array<double, 3> d459;
    double d460;
    double d461;
    double d462;
    double d463;
    double d464;
    std::array<double, 3> d465;
    double d466;
    double d467;
    double d468;
    double d469;
    double d470;
    std::array<double, 3> d471;
    double d472;
    double d473;
    double d474;
    double d475;
    double d476;
    std::array<double, 3> d477;
    double d478;
    double d479;
    double d480;
    double d481;
    double d482;
    std::array<double, 3> d483;
    double d484;
    double d485;
    double d486;
    double d487;
    double d488;
    std::array<double, 3> d489;
    double d490;
    double d491;
    double d492;
    double d493;
    double d494;
    std::array<double, 3> d495;
    double d496;
    double d497;
    double d498;
    double d499;
    double d500;
    std::array<double, 3> d501;
    double d502;
    double d503;
    double d504;
    double d505;
    double d506;
    std::array<double, 3> d507;
    double d508;
    double d509;
    double d510;
    double d511;
    double d512;
    std::array<double, 3> d513;
    double d514;
    double d515;
    double d516;
    double d517;
    double d518;
    std::array<double, 3> d519;
    double d520;
    double d521;
    double d522;
    double d523;
    double d524;
    std::array<double, 3> d525;
    double d526;
    double d527;
    double d528;
    double d529;
    double d530;
    std::array<double, 3> d531;
    double d532;
    double d533;
    double d534;
    double d535;
    double d536;
    std::array<double, 3> d537;
    double d538;
    double d539;
    double d540;
    double d541;
    double d542;
    std::array<double, 3> d543;
    double d544;
    double d545;
    double d546;
    double d547;
    double d548;
    std::array<double, 3> d549;
    double d550;
    double d551;
    double d552;
    double d553;
    double d554;
    std::array<double, 3> d555;
    double d556;
    double d557;
    double d558;
    double d559;
    double d560;
    std::array<double, 3> d561;
    double d562;
    double d563;
    double d564;
    double d565;
    double d566;
    std::array<double, 3> d567;
    double d568;
    double d569;
    double d570;
    double d571;
    double d572;
    std::array<double, 3> d573;
    double d574;
    double d575;
    double d576;
    double d577;
    double d578;
    std::array<double, 3> d579;
    double d580;
    double d581;
    double d582;
    double d583;
    double d584;
    std::array<double, 3> d585;
    double d586;
    double d587;
    double d588;
    double d589;
    double d590;
    std::array<double, 3> d591;
    double d592;
    double d593;
    double d594;
    double d595;
    double d596;
    std::array<double, 3> d597;
    double d598;
    double d599;
    double d600;
    double d601;
    double d602;
    std::array<double, 3> d603;
    double d604;
    double d605;
    double d606;
    double d607;
    double d608;
    std::array<double, 3> d609;
    double d610;
    double d611;
    double d612;
    double d613;
    double d614;
    std::array<double, 3> d615;
    double d616;
    double d617;
    double d618;
    double d619;
    double d620;
    std::array<double, 3> d621;
    double d622;
    double d623;
    double d624;
    double d625;
    double d626;
    std::array<double, 3> d627;
    double d628;
    double d629;
    double d630;
    double d631;
    double d632;
    std::array<double, 3> d633;
    double d634;
    double d635;
    double d636;
    double d637;
    double d638;
    std::array<double, 3> d639;
    double d640;
    double d641;
    double d642;
    double d643;
    double d644;
    std::array<double, 3> d645;
    double d646;
    double d647;
    double d648;
    double d649;
    double d650;
    std::array<double, 3> d651;
    double d652;
    double d653;
    double d654;
    double d655;
    double d656;
    std::array<double, 3> d657;
    double d658;
    double d659;
    double d660;
    double d661;
    double d662;
    std::array<double, 3> d663;
    double d664;
    double d665;
    double d666;
    double d667;
    double d668;
    std::array<double, 3> d669;
    double d670;
    double d671;
    double d672;
    double d673;
    double d674;
    std::array<double, 3> d675;
    double d676;
    double d677;
    double d678;
    double d679;
    double d680;
    std::array<double, 3> d681;
    double d682;
    double d683;
    double d684;
    double d685;
    double d686;
    std::array<double, 3> d687;
    double d688;
    double d689;
    double d690;
    double d691;
    double d692;
    std::array<double, 3> d693;
    double d694;
    double d695;
    double d696;
    double d697;
    double d698;
    std::array<double, 3> d699;
    double d700;
    double d701;
    double d702;
    double d703;
    double d704;
    std::array<double, 3> d705;
    double d706;
    double d707;
    double d708;
    double d709;
    double d710;
    std::array<double, 3> d711;
    double d712;
    double d713;
    double d714;
    double d715;
    double d716;
    std::array<double, 3> d717;
    double d718;
    double d719;
    double d720;
    double d721;
    double d722;
    std::array<double, 3> d723;
    double d724;
    double d725;
    double d726;
    double d727;
    double d728;
    std::array<double, 3> d729;
    double d730;
    double d731;
    double d732;
    double d733;
    double d734;
    std::array<double, 3> d735;
    double d736;
    double d737;
    double d738;
    double d739;
    double d740;
    std::array<double, 3> d741;
    double d742;
    double d743;
    double d744;
    double d745;
    double d746;
    std::array<double, 3> d747;
    double d748;
    double d749;
    double d750;
    double d751;
    double d752;
    std::array<double, 3> d753;
    double d754;
    double d755;
    double d756;
    double d757;
    double d758;
    std::array<double, 3> d759;
    double d760;
    double d761;
    double d762;
    double d763;
    double d764;
    std::array<double, 3> d765;
    double d766;
    double d767;
    double d768;
    double d769;
    double d770;
    std::array<double, 3> d771;
    double d772;
    double d773;
    double d774;
    double d775;
    double d776;
    std::array<double, 3> d777;
    double d778;
    double d779;
    double d780;
    double d781;
    double d782;
    std::array<double, 3> d783;
    double d784;
    double d785;
    double d786;
    double d787;
    double d788;
    std::array<double, 3> d789;
    double d790;
    double d791;
    double d792;
    double d793;
    double d794;
    std::array<double, 3> d795;
    double d796;
    double d797;
    double d798;
    double d799;
    double d800;
    std::array<double, 3> d801;
    double d802;
    double d803;
    double d804;
    double d805;
    double d806;
    std::array<double, 3> d807;
    double d808;
    double d809;
    double d810;
    double d811;
    double d812;
    std::array<double, 3> d813;
    double d814;
    double d815;
    double d816;
    double d817;
    double d818;
    std::array<double, 3> d819;
    double d820;
    double d821;
    double d822;
    double d823;
    double d824;
    std::array<double, 3> d825;
    double d826;
    double d827;
    double d828;
    double d829;
    double d830;
    std::array<double, 3> d831;
    double d832;
    double d833;
    double d834;
    double d835;
    double d836;
    std::array<double, 3> d837;
    double d838;
    double d839;
    double d840;
    double d841;
    double d842;
    std::array<double, 3> d843;
    double d844;
    double d845;
    double d846;
    double d847;
    double d848;
    std::array<double, 3> d849;
    double d850;
    double d851;
    double d852;
    double d853;
    double d854;
    std::array<double, 3> d855;
    double d856;
    double d857;
    double d858;
    double d859;
    double d860;
    std::array<double, 3> d861;
    double d862;
    double d863;
    double d864;
    double d865;
    double d866;
    std::array<double, 3> d867;
    double d868;
    double d869;
    double d870;
    double d871;
    double d872;
    std::array<double, 3> d873;
    double d874;
    double d875;
    double d876;
    double d877;
    double d878;
    std::array<double, 3> d879;
    double d880;
    double d881;
    double d882;
    double d883;
    double d884;
    std::array<double, 3> d885;
    double d886;
    double d887;
    double d888;
    double d889;
    double d890;
    std::array<double, 3> d891;
    double d892;
    double d893;
    double d894;
    double d895;
    double d896;
    std::array<double, 3> d897;
    double d898;
    double d899;
    double d900;
    double d901;
    double d902;
    std::array<double, 3> d903;
    double d904;
    double d905;
    double d906;
    double d907;
    double d908;
    std::array<double, 3> d909;
    double d910;
    double d911;
    double d912;
    double d913;
    double d914;
    std::array<double, 3> d915;
    double d916;
    double d917;
    double d918;
    double d919;
    double d920;
    std::array<double, 3> d921;
    double d922;
    double d923;
    double d924;
    double d925;
    double d926;
    std::array<double, 3> d927;
    double d928;
    double d929;
    double d930;
    double d931;
    double d932;
    std::array<double, 3> d933;
    double d934;
    double d935;
    double d936;
    double d937;
    double d938;
    std::array<double, 3> d939;
    double d940;
    double d941;
    double d942;
    double d943;
    double d944;
    std::array<double, 3> d945;
    double d946;
    double d947;
    double d948;
    double d949;
    double d950;
    std::array<double, 3> d951;
    double d952;
    double d953;
    double d954;
    double d955;
    double d956;
    std::array<double, 3> d957;
    double d958;
    double d959;
    double d960;
    double d961;
    double d962;
    std::array<double, 3> d963;
    double d964;
    double d965;
};

// Solver information
struct CPG_Info_cpp_t {
    double obj_val;
    int iter;
    int status;
    double pri_res;
    double dua_res;
    double time;
};

// Solution and solver information
struct CPG_Result_cpp_t {
    CPG_Prim_cpp_t prim;
    CPG_Dual_cpp_t dual;
    CPG_Info_cpp_t info;
};

// Main solve function
CPG_Result_cpp_t solve_cpp(struct CPG_Updated_cpp_t& CPG_Updated_cpp, struct CPG_Params_cpp_t& CPG_Params_cpp);